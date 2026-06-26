#!/usr/bin/env python3
"""
Fetch OpenCode documentation from the anomalyco/opencode GitHub repo.

Strategy: git sparse-checkout pulls *only* the 34 English `.mdx` files at
`packages/web/src/content/docs/*.mdx` (top-level — language subfolders
ar/de/ru/... are excluded). Each MDX file is then piped through the
Node-based converter at `scripts/mdx_to_md.mjs`, which strips JSX/imports
and emits clean Markdown.

Output mirrors fetch_claude_docs.py / fetch_codex_docs.py: a flat folder
`docs/opencode/` of `.md` files plus a `docs_manifest.json` keyed by
filename with per-file SHA-256 hashes for diff-friendly commits.
"""

from __future__ import annotations

import hashlib
import json
import logging
import os
import re
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)

REPO_URL = "https://github.com/anomalyco/opencode.git"
BRANCH = "dev"  # opencode's default branch is `dev`, not `main`
SPARSE_PATTERN = "/packages/web/src/content/docs/*.mdx"

REPO_ROOT = Path(__file__).resolve().parent.parent
DOCS_DIR = REPO_ROOT / "docs" / "opencode"
CACHE_DIR = REPO_ROOT / ".cache" / "opencode-sparse"
MDX_CONVERTER = REPO_ROOT / "scripts" / "mdx_to_md.mjs"
MANIFEST_FILE = "docs_manifest.json"

# Where the .mdx files land inside the sparse checkout
SPARSE_DOCS_REL = Path("packages/web/src/content/docs")


def run(cmd: list[str], cwd: Path | None = None) -> str:
    """Run a command, raise on failure, return stdout."""
    logger.debug("$ %s", " ".join(cmd))
    proc = subprocess.run(
        cmd,
        cwd=cwd,
        check=True,
        text=True,
        capture_output=True,
    )
    return proc.stdout


def detect_default_branch() -> str:
    """Ask GitHub for the current default branch of the upstream repo.

    Falls back to BRANCH if the API call fails (offline, rate-limited, etc.).
    The opencode repo uses `dev` as its default, but we resolve dynamically
    in case that ever changes.
    """
    try:
        out = run(["git", "ls-remote", "--symref", REPO_URL, "HEAD"])
        # First line looks like: "ref: refs/heads/dev\tHEAD"
        m = re.search(r"refs/heads/(\S+)", out)
        if m:
            return m.group(1)
    except subprocess.CalledProcessError as exc:
        logger.warning("Could not detect default branch via ls-remote: %s", exc.stderr.strip())
    return BRANCH


def setup_sparse_checkout(branch: str) -> Path:
    """Create or refresh the sparse-checkout cache. Returns path to docs dir."""
    if (CACHE_DIR / ".git").exists():
        logger.info("Refreshing existing sparse checkout at %s", CACHE_DIR)
        run(["git", "fetch", "--depth", "1", "origin", branch], cwd=CACHE_DIR)
        run(["git", "reset", "--hard", f"origin/{branch}"], cwd=CACHE_DIR)
    else:
        logger.info("Cloning %s (sparse, blob:none) into %s", REPO_URL, CACHE_DIR)
        if CACHE_DIR.exists():
            shutil.rmtree(CACHE_DIR)
        CACHE_DIR.parent.mkdir(parents=True, exist_ok=True)
        run(
            [
                "git",
                "clone",
                "--filter=blob:none",
                "--no-checkout",
                "--depth",
                "1",
                "--branch",
                branch,
                REPO_URL,
                str(CACHE_DIR),
            ]
        )
        run(["git", "sparse-checkout", "init", "--no-cone"], cwd=CACHE_DIR)
        run(["git", "sparse-checkout", "set", SPARSE_PATTERN], cwd=CACHE_DIR)
        run(["git", "checkout", branch], cwd=CACHE_DIR)

    src = CACHE_DIR / SPARSE_DOCS_REL
    if not src.is_dir():
        raise RuntimeError(f"Sparse checkout produced no docs dir at {src}")
    return src


def list_english_mdx(src: Path) -> list[Path]:
    """Return top-level English .mdx files (sorted). Language subdirs ignored."""
    files = sorted(p for p in src.iterdir() if p.is_file() and p.suffix == ".mdx")
    logger.info("Found %d English .mdx files in %s", len(files), src)
    return files


def convert_mdx(mdx_text: str) -> str:
    """Pipe MDX through the Node converter and return Markdown."""
    proc = subprocess.run(
        ["node", str(MDX_CONVERTER)],
        input=mdx_text,
        text=True,
        capture_output=True,
        check=True,
    )
    return proc.stdout


def mdx_to_md_filename(mdx_path: Path) -> str:
    """index.mdx -> index.md, agents.mdx -> agents.md."""
    return mdx_path.stem + ".md"


def load_manifest() -> dict:
    path = DOCS_DIR / MANIFEST_FILE
    if path.exists():
        try:
            data = json.loads(path.read_text())
            data.setdefault("files", {})
            return data
        except Exception as exc:
            logger.warning("Failed to load manifest: %s", exc)
    return {"files": {}, "last_updated": None}


def save_manifest(manifest: dict, branch: str) -> None:
    path = DOCS_DIR / MANIFEST_FILE
    manifest["last_updated"] = datetime.now().isoformat()

    github_repo = os.environ.get("GITHUB_REPOSITORY", "mrkhachaturov/agent-harness-docs")
    github_ref = os.environ.get("GITHUB_REF_NAME", "main")
    if not re.match(r"^[\w.-]+/[\w.-]+$", github_repo):
        github_repo = "mrkhachaturov/agent-harness-docs"
    if not re.match(r"^[\w.-]+$", github_ref):
        github_ref = "main"

    manifest["base_url"] = (
        f"https://raw.githubusercontent.com/{github_repo}/{github_ref}/docs/opencode/"
    )
    manifest["github_repository"] = github_repo
    manifest["github_ref"] = github_ref
    manifest["upstream_repo"] = REPO_URL
    manifest["upstream_branch"] = branch
    manifest["description"] = (
        "OpenCode documentation manifest. Keys are filenames (converted from "
        "MDX to plain Markdown), append to base_url for raw GitHub URLs."
    )
    path.write_text(json.dumps(manifest, indent=2))


def content_changed(content: str, old_hash: str) -> bool:
    return hashlib.sha256(content.encode("utf-8")).hexdigest() != old_hash


def save_file(filename: str, content: str) -> str:
    (DOCS_DIR / filename).write_text(content, encoding="utf-8")
    return hashlib.sha256(content.encode("utf-8")).hexdigest()


def cleanup_obsolete(current: set[str], old_manifest: dict) -> None:
    previous = set(old_manifest.get("files", {}).keys())
    for stale in previous - current:
        if stale == MANIFEST_FILE:
            continue
        p = DOCS_DIR / stale
        if p.exists():
            logger.info("Removing obsolete: %s", stale)
            p.unlink()


def main() -> int:
    started = datetime.now()
    logger.info("OpenCode docs fetch starting")

    if not MDX_CONVERTER.exists():
        logger.error("MDX converter missing: %s", MDX_CONVERTER)
        return 1
    if shutil.which("node") is None:
        logger.error("Node.js not found in PATH — required for MDX conversion")
        return 1
    if shutil.which("git") is None:
        logger.error("git not found in PATH")
        return 1

    DOCS_DIR.mkdir(parents=True, exist_ok=True)
    logger.info("Output: %s", DOCS_DIR)

    branch = detect_default_branch()
    logger.info("Upstream branch: %s", branch)

    try:
        src = setup_sparse_checkout(branch)
    except subprocess.CalledProcessError as exc:
        logger.error("Sparse checkout failed: %s", exc.stderr.strip())
        return 1

    mdx_files = list_english_mdx(src)
    if not mdx_files:
        logger.error("No .mdx files discovered — sparse pattern may be wrong")
        return 1

    manifest = load_manifest()
    new_manifest: dict = {"files": {}}
    fetched: set[str] = set()
    successful = 0
    failed = 0
    failed_files: list[str] = []

    for i, mdx_path in enumerate(mdx_files, 1):
        rel = mdx_path.relative_to(CACHE_DIR)
        out_name = mdx_to_md_filename(mdx_path)
        logger.info("[%d/%d] %s -> %s", i, len(mdx_files), rel, out_name)
        try:
            mdx_text = mdx_path.read_text(encoding="utf-8")
            md_text = convert_mdx(mdx_text)

            if len(md_text.strip()) < 30:
                raise ValueError(f"converted content suspiciously short ({len(md_text)} bytes)")

            old_hash = manifest.get("files", {}).get(out_name, {}).get("hash", "")
            old_entry = manifest.get("files", {}).get(out_name, {})

            if content_changed(md_text, old_hash):
                file_hash = save_file(out_name, md_text)
                last_updated = datetime.now().isoformat()
                logger.info("Updated: %s", out_name)
            else:
                file_hash = old_hash
                last_updated = old_entry.get("last_updated", datetime.now().isoformat())
                logger.info("Unchanged: %s", out_name)

            upstream_path = f"{SPARSE_DOCS_REL.as_posix()}/{mdx_path.name}"
            upstream_url = f"https://github.com/anomalyco/opencode/blob/{branch}/{upstream_path}"
            new_manifest["files"][out_name] = {
                "upstream_path": upstream_path,
                "upstream_url": upstream_url,
                "hash": file_hash,
                "last_updated": last_updated,
            }
            fetched.add(out_name)
            successful += 1

        except subprocess.CalledProcessError as exc:
            logger.error("MDX conversion failed for %s: %s", mdx_path.name, exc.stderr.strip())
            failed += 1
            failed_files.append(mdx_path.name)
        except Exception as exc:
            logger.error("Failed %s: %s", mdx_path.name, exc)
            failed += 1
            failed_files.append(mdx_path.name)

    cleanup_obsolete(fetched, manifest)

    new_manifest["fetch_metadata"] = {
        "last_fetch_completed": datetime.now().isoformat(),
        "fetch_duration_seconds": (datetime.now() - started).total_seconds(),
        "total_pages_discovered": len(mdx_files),
        "pages_fetched_successfully": successful,
        "pages_failed": failed,
        "failed_files": failed_files,
        "upstream_repo": REPO_URL,
        "upstream_branch": branch,
        "sparse_pattern": SPARSE_PATTERN,
        "total_files": len(fetched),
        "fetch_tool_version": "1.0",
    }

    save_manifest(new_manifest, branch)

    duration = datetime.now() - started
    logger.info("=" * 50)
    logger.info("Done in %s", duration)
    logger.info("Discovered: %d", len(mdx_files))
    logger.info("Successful: %d/%d", successful, len(mdx_files))
    logger.info("Failed:     %d", failed)
    if failed_files:
        for f in failed_files:
            logger.warning("  - %s", f)
        if successful == 0:
            return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
