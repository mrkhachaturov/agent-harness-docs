#!/usr/bin/env python3
"""
Fetch OpenAI Codex documentation from developers.openai.com.

Discovery: /codex/llms.txt — markdown index where every page is listed as
`[Title](https://developers.openai.com/codex/<slug>.md): description`.

Each page is then fetched from its `.md` twin. Vercel anti-bot only blocks
requests without Chrome's `sec-ch-ua` / `sec-fetch` headers, so we send the
full Chrome header set.

Output mirrors fetch_claude_docs.py: a flat folder of `.md` files plus a
`docs_manifest.json` with per-file SHA-256 hashes for diff-friendly commits.
"""

from __future__ import annotations

import hashlib
import json
import logging
import os
import random
import re
import sys
import time
from datetime import datetime
from pathlib import Path

import requests

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)

BASE_URL = "https://developers.openai.com"
INDEX_URL = f"{BASE_URL}/codex/llms.txt"
MANIFEST_FILE = "docs_manifest.json"

# Vercel passes the request when these headers are present together.
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36"
    ),
    "Accept": "text/plain,text/markdown,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "sec-ch-ua": '"Chromium";v="148", "Google Chrome";v="148", "Not/A)Brand";v="99"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"macOS"',
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "Referer": f"{BASE_URL}/codex",
}

MAX_RETRIES = 3
RETRY_DELAY = 2
MAX_RETRY_DELAY = 30
RATE_LIMIT_DELAY = 0.5

# URLs we explicitly skip — bundles or duplicates of single-page content.
SKIP_URLS = {
    f"{BASE_URL}/codex/llms-full.txt",
    f"{BASE_URL}/codex/codex-manual.md",
}

URL_RE = re.compile(
    r"https://developers\.openai\.com/codex/[A-Za-z0-9_\-./]+\.md"
)


def url_to_safe_filename(url: str) -> str:
    """Map a codex doc URL to a flat filename.

    /codex/quickstart.md            -> quickstart.md
    /codex/app/automations.md       -> app__automations.md
    /codex/concepts/sandboxing.md   -> concepts__sandboxing.md
    """
    path = url.split("/codex/", 1)[1]  # "app/automations.md"
    if path.endswith(".md"):
        path = path[:-3]
    safe = path.replace("/", "__")
    return safe + ".md"


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
        f"https://raw.githubusercontent.com/{github_repo}/{github_ref}/docs/codex/"
    )
    manifest["github_repository"] = github_repo
    manifest["github_ref"] = github_ref
    manifest["description"] = (
        "Codex documentation manifest. Keys are filenames, "
        "append to base_url for raw GitHub URLs."
    )
    manifest_path.write_text(json.dumps(manifest, indent=2))


def discover_pages(session: requests.Session) -> list[str]:
    """Return sorted, deduplicated list of codex `.md` URLs from llms.txt."""
    logger.info("Fetching index: %s", INDEX_URL)
    resp = session.get(INDEX_URL, headers=HEADERS, timeout=30)
    resp.raise_for_status()

    urls = sorted({m.group(0) for m in URL_RE.finditer(resp.text)} - SKIP_URLS)
    logger.info("Discovered %d codex pages in llms.txt", len(urls))
    return urls


def validate_markdown(content: str, filename: str) -> None:
    if not content or content.lstrip().startswith(("<!DOCTYPE", "<html")):
        raise ValueError("Received HTML instead of markdown")
    if len(content.strip()) < 30:
        raise ValueError(f"Content too short ({len(content)} bytes)")


def fetch_page(url: str, session: requests.Session) -> tuple[str, str]:
    filename = url_to_safe_filename(url)
    logger.info("Fetching: %s -> %s", url, filename)

    for attempt in range(MAX_RETRIES):
        try:
            resp = session.get(url, headers=HEADERS, timeout=30, allow_redirects=True)

            if resp.status_code == 429:
                wait = int(resp.headers.get("Retry-After", 60))
                logger.warning("Rate limited, sleeping %ds", wait)
                time.sleep(wait)
                continue

            resp.raise_for_status()
            content = resp.text
            validate_markdown(content, filename)
            return filename, content

        except requests.exceptions.RequestException as exc:
            logger.warning(
                "Attempt %d/%d failed for %s: %s",
                attempt + 1, MAX_RETRIES, filename, exc,
            )
            if attempt < MAX_RETRIES - 1:
                delay = min(RETRY_DELAY * (2 ** attempt), MAX_RETRY_DELAY)
                time.sleep(delay * random.uniform(0.5, 1.0))
            else:
                raise

    raise RuntimeError(f"unreachable: exhausted retries for {url}")


def content_changed(content: str, old_hash: str) -> bool:
    return hashlib.sha256(content.encode("utf-8")).hexdigest() != old_hash


def save_page(docs_dir: Path, filename: str, content: str) -> str:
    (docs_dir / filename).write_text(content, encoding="utf-8")
    return hashlib.sha256(content.encode("utf-8")).hexdigest()


def cleanup_obsolete(docs_dir: Path, current: set[str], old_manifest: dict) -> None:
    previous = set(old_manifest.get("files", {}).keys())
    for stale in previous - current:
        if stale == MANIFEST_FILE:
            continue
        p = docs_dir / stale
        if p.exists():
            logger.info("Removing obsolete: %s", stale)
            p.unlink()


def main() -> int:
    started = datetime.now()
    logger.info("Codex docs fetch starting")

    docs_dir = Path(__file__).parent.parent / "docs" / "codex"
    docs_dir.mkdir(parents=True, exist_ok=True)
    logger.info("Output: %s", docs_dir)

    manifest = load_manifest(docs_dir)
    new_manifest = {"files": {}}
    fetched: set[str] = set()
    successful = 0
    failed = 0
    failed_urls: list[str] = []

    with requests.Session() as session:
        try:
            urls = discover_pages(session)
        except Exception as exc:
            logger.error("Index discovery failed: %s", exc)
            return 1

        if not urls:
            logger.error("Empty page list from %s", INDEX_URL)
            return 1

        for i, url in enumerate(urls, 1):
            logger.info("[%d/%d] %s", i, len(urls), url)
            try:
                filename, content = fetch_page(url, session)
                old_hash = manifest.get("files", {}).get(filename, {}).get("hash", "")
                old_entry = manifest.get("files", {}).get(filename, {})

                if content_changed(content, old_hash):
                    file_hash = save_page(docs_dir, filename, content)
                    last_updated = datetime.now().isoformat()
                    logger.info("Updated: %s", filename)
                else:
                    file_hash = old_hash
                    last_updated = old_entry.get("last_updated", datetime.now().isoformat())
                    logger.info("Unchanged: %s", filename)

                new_manifest["files"][filename] = {
                    "original_url": url.replace(".md", ""),
                    "original_md_url": url,
                    "hash": file_hash,
                    "last_updated": last_updated,
                }
                fetched.add(filename)
                successful += 1

                if i < len(urls):
                    time.sleep(RATE_LIMIT_DELAY)

            except Exception as exc:
                logger.error("Failed %s: %s", url, exc)
                failed += 1
                failed_urls.append(url)

    cleanup_obsolete(docs_dir, fetched, manifest)

    new_manifest["fetch_metadata"] = {
        "last_fetch_completed": datetime.now().isoformat(),
        "fetch_duration_seconds": (datetime.now() - started).total_seconds(),
        "total_pages_discovered": len(urls),
        "pages_fetched_successfully": successful,
        "pages_failed": failed,
        "failed_urls": failed_urls,
        "index_url": INDEX_URL,
        "base_url": BASE_URL,
        "total_files": len(fetched),
        "fetch_tool_version": "1.0",
    }

    save_manifest(docs_dir, new_manifest)

    duration = datetime.now() - started
    logger.info("=" * 50)
    logger.info("Done in %s", duration)
    logger.info("Discovered: %d", len(urls))
    logger.info("Successful: %d/%d", successful, len(urls))
    logger.info("Failed:     %d", failed)
    if failed_urls:
        for u in failed_urls:
            logger.warning("  - %s", u)
        if successful == 0:
            return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
