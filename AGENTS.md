# Agent Harness Docs

Local docs mirror for AI coding agents — auto-synced, indexer-agnostic.

Today this repo collects documentation for four coding-agent harnesses:

- **Claude Code** — sourced from `code.claude.com` via sitemap + `.md` twin
- **OpenAI Codex** — sourced from `developers.openai.com/codex/llms.txt` (Vercel-fronted, needs Chrome `sec-ch-ua*` / `sec-fetch-*` headers)
- **OpenCode** — sourced from `github.com/anomalyco/opencode` via `git sparse-checkout` on `packages/web/src/content/docs/*.mdx`, then converted MDX → Markdown by a Node `remark-mdx` pipeline
- **Pi** — sourced from `github.com/earendil-works/pi` via `git sparse-checkout` on `packages/coding-agent/docs/*.md` (already clean Markdown, no conversion needed)

More harnesses to come. Docs update upstream every 3 hours (GitHub
Actions). The installer wires up a launchd job that syncs all four into
the user's home every hour. End users decide how to index/search the
files (Miyo, ripgrep, Cursor index, plain Read — anything works).

## Repo layout

```
agent-harness-docs/
├── docs/
│   ├── claude-code/                   ~140 .md + docs_manifest.json
│   ├── codex/                         ~80 .md + docs_manifest.json
│   ├── opencode/                      ~34 .md + docs_manifest.json
│   └── pi/                            ~27 .md + docs_manifest.json
├── scripts/
│   ├── fetch_claude_docs.py           → writes docs/claude-code/
│   ├── fetch_codex_docs.py            → writes docs/codex/
│   ├── fetch_opencode_docs.py         → writes docs/opencode/
│   ├── fetch_pi_docs.py               → writes docs/pi/
│   ├── mdx_to_md.mjs                  Node MDX → MD converter (used by opencode fetcher)
│   ├── package.json                   Node deps for the converter
│   ├── package-lock.json              committed for reproducible CI installs
│   ├── render_skills.py               renders Jinja2 → SKILL.md
│   └── requirements.txt               requests, Jinja2 (maintainer-only)
├── skills/
│   ├── templates/                     Jinja2 source-of-truth
│   │   ├── claude-code-docs.SKILL.md.j2
│   │   ├── codex-docs.SKILL.md.j2
│   │   ├── opencode-docs.SKILL.md.j2
│   │   └── pi-docs.SKILL.md.j2
│   ├── claude-code-docs/              rendered variants
│   │   ├── plain/SKILL.md             ls/grep/Read flow
│   │   └── miyo/SKILL.md              Miyo MCP flow
│   ├── codex-docs/
│   │   ├── plain/SKILL.md
│   │   └── miyo/SKILL.md
│   ├── opencode-docs/
│   │   ├── plain/SKILL.md
│   │   └── miyo/SKILL.md
│   └── pi-docs/
│       ├── plain/SKILL.md
│       └── miyo/SKILL.md
├── rules/
│   └── claude-code-docs.md            Codex/OpenCode have no rule-file analog; skill metadata is enough
├── install.sh                         macOS-only; quad rsync + indexer-aware skill pick
├── uninstall.sh
└── .github/workflows/update-docs.yml  runs all four fetchers in one job
```

## How users consume this repo

`install.sh` does NOT clone the repo into the user's home. Instead it:

1. Maintains a hidden cache clone at `~/Library/Caches/agent-harness-docs-mirror/`
2. Rsyncs `docs/claude-code/*` → `~/claude-code-docs/` (flat)
3. Rsyncs `docs/codex/*` → `~/codex-docs/` (flat)
4. Rsyncs `docs/opencode/*` → `~/opencode-docs/` (flat)
5. Rsyncs `docs/pi/*` → `~/pi-docs/` (flat)
6. Installs **one** launchd job that re-runs the sync every hour
7. **Detects** the user's indexer (currently: `miyo` or `plain` fallback)
8. Copies skills into the agents' native locations:
   - `~/.claude/skills/claude-code-docs/SKILL.md` (Claude Code)
   - `~/.agents/skills/codex-docs/SKILL.md` (Codex)
   - `~/.agents/skills/opencode-docs/SKILL.md` (shared) + symlink at `~/.claude/skills/opencode-docs`
   - `~/.agents/skills/pi-docs/SKILL.md` (shared) + symlink at `~/.claude/skills/pi-docs`
9. Copies `rules/claude-code-docs.md` → `~/.claude/rules/`
10. If indexer is `miyo`:
   - Registers Miyo MCP with `claude` and `codex` CLIs (idempotent)
   - Merges a Miyo entry into `~/.config/opencode/opencode.json[c]` (idempotent; bails out cleanly if the user's file has comments, printing a paste-able snippet instead)

End users with Miyo then add the four folders to Miyo with labels
`claude-code-docs`, `codex-docs`, `opencode-docs`, `pi-docs`. Users
without an indexer get the `plain` skill variant that tells the agent to
use ls/grep/Read directly.

## Four source-fetching patterns

| Source | Discovery | Per-page URL or method |
|---|---|---|
| Claude Code | `https://code.claude.com/docs/sitemap.xml` | `<page-url>.md` |
| Codex | `https://developers.openai.com/codex/llms.txt` (markdown list) | `https://developers.openai.com/codex/<slug>.md` |
| OpenCode | `git ls-remote` for default branch on `anomalyco/opencode` | `git sparse-checkout` of `/packages/web/src/content/docs/*.mdx` (non-cone), then `mdx_to_md.mjs` |
| Pi | `git ls-remote` for default branch on `earendil-works/pi` | `git sparse-checkout` of `/packages/coding-agent/docs/*.md` (non-cone), direct copy |

Codex pages 403 against bare `curl` — the fetcher sends the full Chrome
header set (`sec-ch-ua`, `sec-ch-ua-mobile`, `sec-ch-ua-platform`,
`sec-fetch-*`); without those Vercel returns "deny". TLS fingerprint is
not checked, just headers.

OpenCode uses Astro Starlight MDX with `import` / `export` statements and
JSX components (`<Tabs>`, `<TabItem>`, `<Card>`, ...). The MDX→MD pipeline
strips imports, unwraps JSX (keeping children), and emits clean Markdown
that any indexer can read. The pipeline lives in `scripts/mdx_to_md.mjs`
and is invoked as a subprocess by `fetch_opencode_docs.py`. Frontmatter,
fenced code, lists, tables, and Starlight directive callouts (`:::tip`,
`:::note`) are preserved.

Pi docs are already clean Markdown — no MDX or HTML conversion is needed.
The fetcher simply sparse-checks out the `.md` files and copies them into
`docs/pi/`.

## Skills — two shared, two per-harness

Each agent scans its own conventional skill location:

- **Claude Code** → `~/.claude/skills/`
- **Codex** → `~/.agents/skills/` (open agent skills standard)
- **OpenCode** → `~/.config/opencode/skills/` (native), `~/.claude/skills/`, AND `~/.agents/skills/` — all three are read

`claude-code-docs` and `codex-docs` are per-harness, so they live in the
agent's own folder — automatic isolation, no leakage between harnesses,
no symlinks needed.

`opencode-docs` and `pi-docs` are **shared**: any harness can use them
when the user asks about OpenCode or Pi while chatting. The canonical
SKILL.md lives at `~/.agents/skills/<docset>/` (which opencode AND codex
pick up natively), and a symlink at `~/.claude/skills/<docset>` exposes
it to Claude Code too.

This is the pattern all cross-harness skills should follow.

## Skill rendering

Skills are written once in `skills/templates/<docset>.SKILL.md.j2` with
Jinja2 `{% if indexer == "miyo" %}…{% else %}…{% endif %}` blocks for the
indexer-specific bits. `scripts/render_skills.py` expands each template
into one file per indexer at `skills/<docset>/<indexer>/SKILL.md`. Those
rendered files are committed to the repo so `install.sh` stays bash-only
— no Python or Node on the user's machine for installation. CI runs
`render_skills.py --check` to guard against template/output drift.

Adding a new indexer:

1. Add the name to `INDEXERS` in `scripts/render_skills.py`.
2. Extend each Jinja2 template with `{% elif indexer == "<new>" %}` blocks.
3. Extend the `detect_indexer()` function in `install.sh`.
4. Run `python scripts/render_skills.py` and commit everything together.

## MDX→MD conversion

The OpenCode fetcher is the only one that needs Node — for MDX parsing.
The Node side is fully isolated:

- `scripts/package.json` lists deps (`unified`, `remark-parse`,
  `remark-mdx`, `remark-gfm`, `remark-stringify`, `unist-util-visit`,
  `mdast-util-to-string`)
- `scripts/package-lock.json` is committed so CI reproduces exactly
- CI runs `npm ci` inside `scripts/` before invoking the fetcher
- `scripts/mdx_to_md.mjs` reads MDX from stdin, emits Markdown on stdout
- `fetch_opencode_docs.py` calls `node scripts/mdx_to_md.mjs` per file
- End users (running `install.sh`) never see Node — they just rsync the
  pre-converted `.md` files

## Key files

@install.sh
@uninstall.sh
@scripts/fetch_claude_docs.py
@scripts/fetch_codex_docs.py
@scripts/fetch_opencode_docs.py
@scripts/fetch_pi_docs.py
@scripts/mdx_to_md.mjs
@scripts/render_skills.py
@skills/templates/claude-code-docs.SKILL.md.j2
@skills/templates/codex-docs.SKILL.md.j2
@skills/templates/opencode-docs.SKILL.md.j2
@skills/templates/pi-docs.SKILL.md.j2
@rules/claude-code-docs.md
@.github/workflows/update-docs.yml
