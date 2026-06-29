#!/usr/bin/env python3
"""
Fetch Cursor documentation from cursor.com.

Discovery: /llms.txt (at the site root, NOT under /docs) — a curated Markdown
index that lists every page as a bare `https://cursor.com/.../<slug>.md` URL,
grouped under `##` section headings. Each page is then fetched from its `.md`
twin (Mintlify-on-Vercel serves a clean Markdown twin for every doc page).

Why this fetcher is concurrent + multi-pass (unlike the other four):
    Cursor's `.md` twins are generated lazily. A *cold* page (never rendered)
    returns **404** on first hit and only flips to 200 once it has been warmed;
    repeated access triggers generation. A naive sequential fetch with
    retry-backoff therefore (a) crawls through 183 pages one at a time and
    (b) wastes long backoff windows on cold-404s that won't recover in ~5s.

    Instead we fetch concurrently with a thread pool (the warm majority finish
    in a couple seconds), collect the cold-404 misses, pause to let them warm,
    and retry just those in subsequent passes. A 404 is never retried inside a
    single pass — it's deferred to the next warming pass.

Layout: unlike the other four (flat, `__`-joined), this fetcher mirrors the
site's own category hierarchy as real subfolders under `docs/cursor/`:

    https://cursor.com/docs.md                      -> docs/cursor/index.md
    https://cursor.com/docs/agent/overview.md       -> docs/cursor/agent/overview.md
    https://cursor.com/docs/agent/tools/terminal.md -> docs/cursor/agent/tools/terminal.md
    https://cursor.com/changelog.md                 -> docs/cursor/changelog.md

This is the new layout convention; the other docsets will migrate to it over
time. Output carries a `docs_manifest.json` at the docset root with per-file
SHA-256 hashes (keys are POSIX-relative paths) for diff-friendly commits.
"""

from __future__ import annotations

import hashlib
import json
import logging
import os
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from pathlib import Path

import requests

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)

BASE_URL = "https://cursor.com"
INDEX_URL = f"{BASE_URL}/llms.txt"
MANIFEST_FILE = "docs_manifest.json"

# Minimal browser-ish headers. Cursor is Vercel-fronted but does NOT gate on the
# Chrome `sec-ch-ua` / `sec-fetch` set (a plain UA passes); `Accept: */*` matches
# what works and avoids any content-negotiation surprises.
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36"
    ),
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": f"{BASE_URL}/docs",
}

# Concurrency + warming-pass tuning. The server handles ~16 concurrent fine
# (verified); 10 is a polite default. Cold-404 pages are retried in later passes
# after a pause that gives Mintlify time to generate them.
MAX_WORKERS = 10
TIMEOUT = 30
PASS_WAITS = [0, 6, 15, 30]  # seconds to wait before pass 0,1,2,3 (len ⇒ max passes)
TRANSPORT_RETRY = 2  # quick in-pass retries for network blips / 429 / 5xx only

# llms.txt has shipped a malformed entry: the URL prefix is duplicated, e.g.
# `https://cursor.comhttps://cursor.com/changelog.md`. Collapse it before the
# regex pass so URL extraction stays clean.
MALFORMED_PREFIX = "cursor.comhttps://cursor.com"

# URLs to drop. `/changelog.md` is the (de-duplicated) malformed entry — it has
# no real Markdown twin and just serves 800 KB of marketing-site HTML, so there
# is nothing to mirror. The changelog lives only as an HTML SPA page, not on a
# public docs repo, so we skip it rather than scrape HTML.
SKIP_URLS = {f"{BASE_URL}/changelog.md"}

URL_RE = re.compile(r"https://cursor\.com/[A-Za-z0-9_\-./]+\.md")

# English-only: localized pages are served under a 2-letter language-code prefix
# (`/es/…`, `/fr/…`, `/ja/…`, …). English docs live under `/docs/…`, `/help/…`,
# or as root `*.md` files — none of which have a 2-letter first path segment.
# Matching the segment generically keeps new locales (de, zh, ko, …) out too.
LOCALE_SEG_RE = re.compile(r"^[a-z]{2}$")


def _is_localized(url: str) -> bool:
    first_seg = url.split("cursor.com/", 1)[1].split("/", 1)[0]
    return LOCALE_SEG_RE.match(first_seg) is not None


class ColdMiss(Exception):
    """A 404 we attribute to a not-yet-generated (.md) page — retry next pass."""


def url_to_relpath(url: str) -> str:
    """Map a Cursor doc URL to a POSIX-relative path under docs/cursor/.

    The leading `docs/` segment is dropped so categories sit at the docset
    root; the bare `/docs.md` root page becomes `index.md`. Non-`/docs` pages
    (e.g. `/changelog.md`) keep their own top-level path.

        https://cursor.com/docs.md                -> index.md
        https://cursor.com/docs/agent/overview.md -> agent/overview.md
        https://cursor.com/docs/models/gpt-5-5.md -> models/gpt-5-5.md
        https://cursor.com/changelog.md           -> changelog.md
    """
    path = url.split("cursor.com/", 1)[1]  # "docs/agent/overview.md" | "docs.md"
    if path.endswith(".md"):
        path = path[:-3]
    if path == "docs":
        return "index.md"
    if path.startswith("docs/"):
        path = path[len("docs/") :]
    return path + ".md"


def load_manifest(docs_dir: Path) -> dict:
    manifest_path = docs_dir / MANIFEST_FILE
    if manifest_path.exists():
        try:
            data = json.loads(manifest_path.read_text())
            data.setdefault("files", {})
            return data
        except Exception as exc:
            logger.warning("Failed to load manifest: %s", exc)
    return {"files": {}, "last_updated": None}


def save_manifest(docs_dir: Path, manifest: dict) -> None:
    manifest_path = docs_dir / MANIFEST_FILE
    manifest["last_updated"] = datetime.now().isoformat()

    github_repo = os.environ.get("GITHUB_REPOSITORY", "mrkhachaturov/agent-harness-docs")
    github_ref = os.environ.get("GITHUB_REF_NAME", "main")

    if not re.match(r"^[\w.-]+/[\w.-]+$", github_repo):
        github_repo = "mrkhachaturov/agent-harness-docs"
    if not re.match(r"^[\w.-]+$", github_ref):
        github_ref = "main"

    manifest["base_url"] = (
        f"https://raw.githubusercontent.com/{github_repo}/{github_ref}/docs/cursor/"
    )
    manifest["github_repository"] = github_repo
    manifest["github_ref"] = github_ref
    manifest["description"] = (
        "Cursor documentation manifest. Keys are POSIX-relative paths under "
        "docs/cursor/ (nested by the site's own category hierarchy); append to "
        "base_url for raw GitHub URLs."
    )
    manifest_path.write_text(json.dumps(manifest, indent=2))


def discover_pages(session: requests.Session) -> list[str]:
    """Return a sorted, deduplicated list of Cursor `.md` URLs from llms.txt."""
    logger.info("Fetching index: %s", INDEX_URL)
    resp = session.get(INDEX_URL, headers=HEADERS, timeout=TIMEOUT)
    resp.raise_for_status()

    # Repair the duplicated-prefix entry before extracting URLs, drop the known
    # non-markdown entries (SKIP_URLS), and keep English only (exclude the
    # language-code-prefixed localized pages).
    text = resp.text.replace(MALFORMED_PREFIX, "cursor.com")
    urls = sorted(u for u in set(URL_RE.findall(text)) - SKIP_URLS if not _is_localized(u))
    logger.info("Discovered %d Cursor pages in llms.txt", len(urls))
    return urls


def validate_markdown(content: str) -> None:
    if not content or content.lstrip().startswith(("<!DOCTYPE", "<html")):
        raise ValueError("Received HTML instead of markdown")
    if len(content.strip()) < 30:
        raise ValueError(f"Content too short ({len(content)} bytes)")


def fetch_one(url: str, session: requests.Session) -> tuple[str, str]:
    """Fetch a single page. Returns (relpath, content).

    Raises ColdMiss on 404 (defer to the next warming pass). Transient transport
    errors (connection/timeout, 429, 5xx) get a couple of quick in-pass retries.
    """
    relpath = url_to_relpath(url)
    last_exc: Exception | None = None

    for attempt in range(TRANSPORT_RETRY + 1):
        try:
            resp = session.get(url, headers=HEADERS, timeout=TIMEOUT, allow_redirects=True)
        except requests.exceptions.RequestException as exc:
            last_exc = exc
            time.sleep(1.5 * (attempt + 1))
            continue

        if resp.status_code == 404:
            raise ColdMiss(relpath)
        if resp.status_code == 429 or resp.status_code >= 500:
            wait = int(resp.headers.get("Retry-After", 3))
            last_exc = requests.exceptions.HTTPError(f"{resp.status_code} for {url}")
            time.sleep(wait)
            continue

        resp.raise_for_status()
        validate_markdown(resp.text)
        return relpath, resp.text

    raise last_exc or RuntimeError(f"unreachable: {url}")


def fetch_all(urls: list[str]) -> tuple[dict[str, str], list[str]]:
    """Concurrent multi-pass fetch. Returns ({relpath: content}, failed_urls)."""
    results: dict[str, str] = {}
    todo = list(urls)

    for pass_i, wait in enumerate(PASS_WAITS):
        if not todo:
            break
        if wait:
            logger.info(
                "Warming pass %d: %d page(s) still cold, waiting %ds…",
                pass_i,
                len(todo),
                wait,
            )
            time.sleep(wait)

        cold: list[str] = []
        errored: list[str] = []
        # One session shared across the pool — fine for plain concurrent GETs.
        with requests.Session() as session, ThreadPoolExecutor(max_workers=MAX_WORKERS) as ex:
            futures = {ex.submit(fetch_one, u, session): u for u in todo}
            for fut in as_completed(futures):
                url = futures[fut]
                try:
                    relpath, content = fut.result()
                    results[relpath] = content
                except ColdMiss:
                    cold.append(url)
                except Exception as exc:
                    logger.warning("pass %d: %s — %s", pass_i, url, exc)
                    errored.append(url)

        done = len(todo) - len(cold) - len(errored)
        logger.info(
            "Pass %d done: %d ok, %d cold(404), %d errored",
            pass_i,
            done,
            len(cold),
            len(errored),
        )
        # Retry both cold and errored in the next pass (transient either way).
        todo = cold + errored

    return results, todo


def cleanup_obsolete(docs_dir: Path, current: set[str], old_manifest: dict) -> None:
    """Remove files we previously fetched but no longer see, then prune the
    empty directories the nested layout leaves behind."""
    previous = set(old_manifest.get("files", {}).keys())
    for stale in previous - current:
        if stale == MANIFEST_FILE:
            continue
        p = docs_dir / stale
        if p.exists():
            logger.info("Removing obsolete: %s", stale)
            p.unlink()

    # Prune now-empty category directories (deepest first), never the root.
    for d in sorted(
        (p for p in docs_dir.rglob("*") if p.is_dir()),
        key=lambda p: len(p.parts),
        reverse=True,
    ):
        if not any(d.iterdir()):
            logger.info("Removing empty dir: %s", d.relative_to(docs_dir))
            d.rmdir()


def main() -> int:
    started = datetime.now()
    logger.info("Cursor docs fetch starting")

    docs_dir = Path(__file__).parent.parent / "docs" / "cursor"
    docs_dir.mkdir(parents=True, exist_ok=True)
    logger.info("Output: %s", docs_dir)

    manifest = load_manifest(docs_dir)

    with requests.Session() as session:
        try:
            urls = discover_pages(session)
        except Exception as exc:
            logger.error("Index discovery failed: %s", exc)
            return 1
    if not urls:
        logger.error("Empty page list from %s", INDEX_URL)
        return 1

    results, failed_urls = fetch_all(urls)

    # Write files + build manifest single-threaded (fetch was concurrent).
    new_manifest: dict = {"files": {}}
    by_relpath = {url_to_relpath(u): u for u in urls}
    for relpath, content in sorted(results.items()):
        new_hash = hashlib.sha256(content.encode("utf-8")).hexdigest()
        old_entry = manifest.get("files", {}).get(relpath, {})
        if new_hash != old_entry.get("hash", ""):
            out = docs_dir / relpath
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(content, encoding="utf-8")
            last_updated = datetime.now().isoformat()
            logger.info("Updated: %s", relpath)
        else:
            last_updated = old_entry.get("last_updated", datetime.now().isoformat())

        url = by_relpath.get(relpath, f"{BASE_URL}/{relpath}")
        new_manifest["files"][relpath] = {
            "original_url": url.replace(".md", ""),
            "original_md_url": url,
            "hash": new_hash,
            "last_updated": last_updated,
        }

    cleanup_obsolete(docs_dir, set(results), manifest)

    new_manifest["fetch_metadata"] = {
        "last_fetch_completed": datetime.now().isoformat(),
        "fetch_duration_seconds": (datetime.now() - started).total_seconds(),
        "total_pages_discovered": len(urls),
        "pages_fetched_successfully": len(results),
        "pages_failed": len(failed_urls),
        "failed_urls": sorted(failed_urls),
        "index_url": INDEX_URL,
        "base_url": BASE_URL,
        "total_files": len(results),
        "layout": "nested",
        "max_workers": MAX_WORKERS,
        "warming_passes": len(PASS_WAITS),
        "fetch_tool_version": "2.0",
    }

    save_manifest(docs_dir, new_manifest)

    duration = datetime.now() - started
    logger.info("=" * 50)
    logger.info("Done in %s", duration)
    logger.info("Discovered: %d", len(urls))
    logger.info("Successful: %d/%d", len(results), len(urls))
    logger.info("Failed:     %d", len(failed_urls))
    if failed_urls:
        for u in sorted(failed_urls):
            logger.warning("  - %s", u)
        if not results:
            return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
