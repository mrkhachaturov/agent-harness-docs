# Claude Code Documentation Mirror

[![Last Update](https://img.shields.io/github/last-commit/mrkhachaturov/claude-code-docs/main.svg?label=docs%20updated)](https://github.com/mrkhachaturov/claude-code-docs/commits/main)
[![Platform](https://img.shields.io/badge/platform-macOS-blue)](https://github.com/mrkhachaturov/claude-code-docs)

Local mirror of [Claude Code documentation](https://docs.anthropic.com/en/docs/claude-code/), optimized for use with [Miyo](https://miyo.md) local semantic search. Docs update automatically via GitHub Actions; an hourly launchd job mirrors them into a flat folder Miyo can index.

Based on [ericbuess/claude-code-docs](https://github.com/ericbuess/claude-code-docs).

## What the installer sets up

- `~/claude-code-docs/` — flat folder with the doc files (no `docs/` subfolder, no `.git`)
- `~/Library/Caches/claude-code-docs-mirror/` — cache clone of this repo
- `~/Library/Application Support/claude-code-docs/sync.sh` — sync script
- `~/Library/LaunchAgents/com.mrkhachaturovclaude-code-docs.plist` — hourly job
- `~/.claude/skills/claude-code-docs/SKILL.md` — Miyo-backed skill
- `~/.claude/rules/claude-code-docs.md` — always-on hint to use the skill

You then point Miyo at `~/claude-code-docs/` and label it `claude-code-docs`.

## Install

```bash
curl -fsSL https://raw.githubusercontent.com/mrkhachaturov/claude-code-docs/main/install.sh | bash
```

macOS only (uses launchd). Requires `git`, `rsync`, `curl`, and a working [Miyo](https://miyo.md) install if you want the skill to work end-to-end.

After install: open Miyo → add `~/claude-code-docs/` as an indexed folder (label `claude-code-docs`). Restart Claude Code.

## Use

```text
/claude-code-docs how do hooks interact with permissions?
/claude-code-docs explain "sandbox environments"
/claude-code-docs path "permissions" "sandboxing"
```

The skill wraps `mcp__miyo__search` with the required `folder_path: "claude-code-docs"` scope so results never leak from other indexed folders.

The installed rule means Claude consults the local mirror automatically — no slash command needed.

## Update

```bash
curl -fsSL https://raw.githubusercontent.com/mrkhachaturov/claude-code-docs/main/install.sh | bash
```

(Idempotent — re-running just re-pulls and re-wires the launchd job.)

Docs themselves refresh every hour without manual action.

## Uninstall

```bash
curl -fsSL https://raw.githubusercontent.com/mrkhachaturov/claude-code-docs/main/uninstall.sh | bash
```

## License

Documentation content belongs to Anthropic. Installer + skill are open source.
