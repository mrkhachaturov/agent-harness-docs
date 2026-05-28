#!/usr/bin/env python3
"""
Render skill templates to per-indexer SKILL.md files.

For each docset template at `skills/templates/<docset>.SKILL.md.j2`, render
one output per supported indexer at `skills/<docset>/<indexer>/SKILL.md`.

Run this every time you edit a template. CI verifies the rendered output is
in sync (renders, diffs, fails the build if it differs from what's committed).

Usage:
    python scripts/render_skills.py
    python scripts/render_skills.py --check   # exit 1 if any output differs
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, StrictUndefined

REPO_ROOT = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = REPO_ROOT / "skills" / "templates"
SKILLS_DIR = REPO_ROOT / "skills"

INDEXERS = ["plain", "miyo"]

# Map template filename -> docset folder name under skills/
TEMPLATES = {
    "claude-code-docs.SKILL.md.j2": "claude-code-docs",
    "codex-docs.SKILL.md.j2":       "codex-docs",
    "opencode-docs.SKILL.md.j2":    "opencode-docs",
    "pi-docs.SKILL.md.j2":          "pi-docs",
}


def render_all() -> list[tuple[Path, str]]:
    """Render every template × indexer combination. Returns list of (path, content)."""
    env = Environment(
        loader=FileSystemLoader(TEMPLATES_DIR),
        undefined=StrictUndefined,
        keep_trailing_newline=True,
        trim_blocks=True,
        lstrip_blocks=True,
    )

    rendered: list[tuple[Path, str]] = []
    for template_name, docset in TEMPLATES.items():
        template = env.get_template(template_name)
        for indexer in INDEXERS:
            out_path = SKILLS_DIR / docset / indexer / "SKILL.md"
            content = template.render(indexer=indexer, docset=docset)
            rendered.append((out_path, content))
    return rendered


def write_outputs(rendered: list[tuple[Path, str]]) -> None:
    for path, content in rendered:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        print(f"wrote {path.relative_to(REPO_ROOT)}")


def check_outputs(rendered: list[tuple[Path, str]]) -> int:
    """Return 0 if all on-disk outputs match the rendered content, else 1."""
    drift = 0
    for path, expected in rendered:
        if not path.exists():
            print(f"MISSING: {path.relative_to(REPO_ROOT)}")
            drift += 1
            continue
        actual = path.read_text(encoding="utf-8")
        if actual != expected:
            print(f"DRIFT:   {path.relative_to(REPO_ROOT)}")
            drift += 1
    if drift:
        print(f"\n{drift} file(s) out of sync — re-run: python scripts/render_skills.py")
        return 1
    print(f"All {len(rendered)} rendered files match templates.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="Verify on-disk outputs match the rendered content (don't write).",
    )
    args = parser.parse_args()

    rendered = render_all()
    if args.check:
        return check_outputs(rendered)
    write_outputs(rendered)
    return 0


if __name__ == "__main__":
    sys.exit(main())
