# Agent Harness Docs

[![Last Update](https://img.shields.io/github/last-commit/mrkhachaturov/agent-harness-docs/main.svg?label=docs%20updated)](https://github.com/mrkhachaturov/agent-harness-docs/commits/main)
[![Platform](https://img.shields.io/badge/platform-macOS-blue)](https://github.com/mrkhachaturov/agent-harness-docs)

Local docs mirror for AI coding agents — auto-synced, indexer-agnostic.

Today this repo collects documentation for two coding-agent harnesses:

- **Claude Code** — from [code.claude.com](https://code.claude.com/docs/en/overview)
- **OpenAI Codex** — from [developers.openai.com/codex](https://developers.openai.com/codex)

More harnesses will be added over time (Cursor, Aider, etc.). The docs
update upstream every 3 hours via GitHub Actions; an hourly launchd job
mirrors them into flat folders under your home directory.

You decide how to consume them: drop a semantic-search tool on top, grep
the folder, or just let your agent read files directly. The installer
ships a small skill that adapts to whichever indexing tool you have.

> Originally [`claude-code-docs`](https://github.com/ericbuess/claude-code-docs).
> Forked from [ericbuess/claude-code-docs](https://github.com/ericbuess/claude-code-docs)
> and generalised to multiple harnesses + indexers.

## What the installer sets up

| Path | Contents |
|---|---|
| `~/claude-code-docs/` | Claude Code docs (~140 flat `.md` files) |
| `~/codex-docs/` | Codex docs (~80 flat `.md` files) |
| `~/Library/Caches/agent-harness-docs-mirror/` | Cache clone of this repo |
| `~/Library/Application Support/agent-harness-docs/sync.sh` | Sync script |
| `~/Library/LaunchAgents/com.mrkhachaturov.agent-harness-docs.plist` | Hourly launchd job |
| `~/.claude/skills/claude-code-docs/SKILL.md` | Claude Code skill (variant picked by installer) |
| `~/.claude/rules/claude-code-docs.md` | Always-on hint for Claude Code |
| `~/.agents/skills/codex-docs/SKILL.md` | Codex skill (agentskills.io USER scope) |

## Skills adapt to your indexer

At install time the script detects what's on your machine and installs the
matching skill variant from `skills/<docset>/<indexer>/SKILL.md`:

| Detected | Variant | What the skill tells the agent |
|---|---|---|
| [Miyo](https://miyo.md) CLI is on `$PATH` | `miyo` | Use `mcp__miyo__search` with `folder_path: "<docset>"` |
| Nothing | `plain` | Use `ls` / `grep` / `Read` against the docs folder directly |

If you install (or remove) an indexer later, just re-run `install.sh` —
it's idempotent and will swap in the right variant.

> **Want another indexer?** PR welcome — add `<indexer>` to `INDEXERS` in
> [`scripts/render_skills.py`](scripts/render_skills.py) and extend the
> Jinja2 templates in [`skills/templates/`](skills/templates/) with the
> tool-specific blocks. Run `python scripts/render_skills.py` and commit
> both the template change and the rendered output.

## Install

```bash
curl -fsSL https://raw.githubusercontent.com/mrkhachaturov/agent-harness-docs/main/install.sh | bash
```

macOS only for now (uses launchd). Requires `git`, `rsync`, and `curl` —
no Python on your machine.

> Linux / Windows installers are planned. For now, the doc-fetch and
> render scripts work cross-platform; only `install.sh` is mac-specific.

After install, if you're on the `miyo` variant: open Miyo, add the two
doc folders, label them `claude-code-docs` and `codex-docs`. Restart your
agent so the skills/rules load.

## Use

Claude Code:

```text
/claude-code-docs how do hooks interact with permissions?
/claude-code-docs explain "sandbox environments"
/claude-code-docs path "permissions" "sandboxing"
```

Codex (skill is auto-discovered via metadata — no rule file needed):

```text
/codex-docs how do I configure AGENTS.md for nested directories?
/codex-docs explain "skills vs plugins"
/codex-docs path "MCP" "hooks"
```

Each skill scopes its search to its own indexed folder so results never
cross-contaminate.

## How it stays current

- **Upstream** (this repo, GitHub Actions): every 3 hours, two fetchers
  (`scripts/fetch_claude_docs.py`, `scripts/fetch_codex_docs.py`) read the
  upstream sitemaps and update `docs/claude-code/` and `docs/codex/`.
- **Local** (your machine, launchd): every hour, the sync script pulls the
  latest cache clone and rsyncs both subfolders into your two home folders.

## Update

```bash
curl -fsSL https://raw.githubusercontent.com/mrkhachaturov/agent-harness-docs/main/install.sh | bash
```

Idempotent — re-running just re-pulls the cache, re-wires the launchd
job, and re-picks the indexer variant. Docs themselves refresh every hour
without manual action.

## Uninstall

```bash
curl -fsSL https://raw.githubusercontent.com/mrkhachaturov/agent-harness-docs/main/uninstall.sh | bash
```

Removes all installed files and the launchd job. **Does not** remove Miyo
MCP registrations on agent CLIs — those may be used for other things. To
remove them too:

```bash
claude mcp remove miyo
codex  mcp remove miyo
```

## Layout choice — why two skills, two folders

Each agent only scans its own conventional skill locations:

- Claude Code → `~/.claude/skills/`
- Codex → `~/.agents/skills/` (per [agentskills.io](https://agentskills.io) USER scope)

So putting harness-specific skills in each agent's native folder gives
**automatic isolation** (Codex never sees `claude-code-docs`, Claude never
sees `codex-docs`) AND **compliance** with each tool's official path.

General-purpose skills meant for both agents would go in
`~/.agents/skills/<name>/`, then symlinked into `~/.claude/skills/<name>`
so Claude Code picks them up too. That's outside the scope of this repo
for now.

## Maintainer workflow

To add/edit a skill variant: edit the Jinja2 template in
`skills/templates/`, then:

```bash
python scripts/render_skills.py             # render all combinations
python scripts/render_skills.py --check     # verify on-disk matches templates
```

Commit both the template change and the rendered output. CI runs
`--check` and fails the build if they're out of sync.

## License

Documentation content belongs to Anthropic (Claude Code) and OpenAI
(Codex) respectively. Installer, skills, and renderer are open source.
