# Claude Code Documentation Mirror

Local mirror of the official Claude Code documentation, optimized for use
with [Miyo](https://miyo.md) local semantic search.

Docs are kept in `docs/` and updated upstream via GitHub Actions
(see `scripts/fetch_claude_docs.py`).

## How users consume this repo

`install.sh` does NOT clone the repo into the user's home. Instead it:

1. Maintains a hidden cache clone at `~/Library/Caches/claude-code-docs-mirror/`
2. Rsyncs `docs/*` into `~/claude-code-docs/` (flat, no subfolders)
3. Installs a launchd job that re-runs the sync every hour
4. Copies `skills/claude-code-docs/SKILL.md` → `~/.claude/skills/claude-code-docs/`
5. Copies `rules/claude-code-docs.md` → `~/.claude/rules/`

The user then points Miyo at `~/claude-code-docs/` (labelled
`claude-code-docs`) and Miyo handles the embedding + reranking. The
shipped skill calls `mcp__miyo__search` with the required
`folder_path: "claude-code-docs"` scope.

## Key files

@install.sh
@uninstall.sh
@skills/claude-code-docs/SKILL.md
@rules/claude-code-docs.md
@scripts/fetch_claude_docs.py
