# Agent Harness Docs

Local docs mirror for AI coding agents — auto-synced, indexer-agnostic.

Today this repo collects documentation for two coding-agent harnesses:

- **Claude Code** — sourced from `code.claude.com` via sitemap + `.md` twin
- **OpenAI Codex** — sourced from `developers.openai.com/codex/llms.txt` (Vercel-fronted, needs Chrome `sec-ch-ua*` / `sec-fetch-*` headers)

More harnesses to come. Docs update upstream every 3 hours (GitHub
Actions). The installer wires up a launchd job that syncs both into the
user's home every hour. End users decide how to index/search the files
(Miyo, ripgrep, Cursor index, plain Read — anything works).

## Repo layout

```
agent-harness-docs/
├── docs/
│   ├── claude-code/                   ~140 .md + docs_manifest.json
│   └── codex/                         ~80 .md + docs_manifest.json
├── scripts/
│   ├── fetch_claude_docs.py           → writes docs/claude-code/
│   ├── fetch_codex_docs.py            → writes docs/codex/
│   ├── render_skills.py               renders Jinja2 → SKILL.md
│   └── requirements.txt               requests, Jinja2 (maintainer-only)
├── skills/
│   ├── templates/                     Jinja2 source-of-truth
│   │   ├── claude-code-docs.SKILL.md.j2
│   │   └── codex-docs.SKILL.md.j2
│   ├── claude-code-docs/              rendered variants
│   │   ├── plain/SKILL.md             ls/grep/Read flow
│   │   └── miyo/SKILL.md              Miyo MCP flow
│   └── codex-docs/
│       ├── plain/SKILL.md
│       └── miyo/SKILL.md
├── rules/
│   └── claude-code-docs.md            Codex has no rule-file analog; skill metadata is enough
├── install.sh                         macOS-only; dual rsync + indexer-aware skill pick
├── uninstall.sh
└── .github/workflows/update-docs.yml  runs both fetchers in one job
```

## How users consume this repo

`install.sh` does NOT clone the repo into the user's home. Instead it:

1. Maintains a hidden cache clone at `~/Library/Caches/agent-harness-docs-mirror/`
2. Rsyncs `docs/claude-code/*` → `~/claude-code-docs/` (flat)
3. Rsyncs `docs/codex/*` → `~/codex-docs/` (flat)
4. Installs **one** launchd job that re-runs the sync every hour
5. **Detects** the user's indexer (currently: `miyo` or `plain` fallback)
6. Copies the matching `skills/<docset>/<indexer>/SKILL.md` → `~/.claude/skills/claude-code-docs/SKILL.md` and `~/.agents/skills/codex-docs/SKILL.md`
7. Copies `rules/claude-code-docs.md` → `~/.claude/rules/`
8. If indexer is `miyo`: registers Miyo MCP with both `claude` and `codex` CLIs (idempotent)

End users with Miyo then add the two folders to Miyo with labels
`claude-code-docs` and `codex-docs`. Users without an indexer get the
`plain` skill that tells the agent to use ls/grep/Read directly.

## Two key URL patterns

| Source | Index | Per-page markdown URL |
|---|---|---|
| Claude Code | `https://code.claude.com/docs/sitemap.xml` | `<page-url>.md` |
| Codex | `https://developers.openai.com/codex/llms.txt` (markdown list) | `https://developers.openai.com/codex/<slug>.md` |

Codex pages 403 against bare `curl`. The fetcher sends the full Chrome
header set (`sec-ch-ua`, `sec-ch-ua-mobile`, `sec-ch-ua-platform`,
`sec-fetch-*`) — without those Vercel returns "deny". TLS fingerprint is
not checked, just headers.

## Why two skills in two different folders

Each agent only scans its own conventional skill locations:

- Claude Code → `~/.claude/skills/`
- Codex → `~/.agents/skills/` (open agent skills standard)

Putting `claude-code-docs` and `codex-docs` in their respective native
folders gives **automatic isolation** (Codex never sees `claude-code-docs`,
Claude never sees `codex-docs`) AND **compliance** with each tool's
official convention. No symlinks needed.

Future "shared" skills (general-purpose, applicable to both agents) go in
`~/.agents/skills/<skill>/`, then symlinked into `~/.claude/skills/<skill>`
for Claude Code pickup.

## Skill rendering

Skills are written once in `skills/templates/<docset>.SKILL.md.j2` with
Jinja2 `{% if indexer == "miyo" %}…{% else %}…{% endif %}` blocks for the
indexer-specific bits. `scripts/render_skills.py` expands each template
into one file per indexer at `skills/<docset>/<indexer>/SKILL.md`. Those
rendered files are committed to the repo so `install.sh` stays bash-only
— no Python on the user's machine. CI runs `render_skills.py --check` to
guard against template/output drift.

Adding a new indexer:

1. Add the name to `INDEXERS` in `scripts/render_skills.py`.
2. Extend each Jinja2 template with `{% elif indexer == "<new>" %}` blocks.
3. Extend the `detect_indexer()` function in `install.sh`.
4. Run `python scripts/render_skills.py` and commit everything together.

## Key files

@install.sh
@uninstall.sh
@scripts/fetch_claude_docs.py
@scripts/fetch_codex_docs.py
@scripts/render_skills.py
@skills/templates/claude-code-docs.SKILL.md.j2
@skills/templates/codex-docs.SKILL.md.j2
@rules/claude-code-docs.md
@.github/workflows/update-docs.yml
