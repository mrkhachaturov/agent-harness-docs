# Agent Harness Docs

Local docs mirror for AI coding agents, consumed through per-agent skills that
search the docs with [Miyo](https://miyo.md).

This repo collects documentation for five coding-agent harnesses:

- **Claude Code** — sourced from `code.claude.com` via sitemap + `.md` twin
- **OpenAI Codex** — sourced from `developers.openai.com/codex/llms.txt` (Vercel-fronted, needs Chrome `sec-ch-ua*` / `sec-fetch-*` headers)
- **Cursor** — sourced from `cursor.com/llms.txt` (Mintlify-on-Vercel) via `.md` twin per page; no anti-bot headers needed
- **OpenCode** — sourced from `github.com/anomalyco/opencode` via `git sparse-checkout` on `packages/web/src/content/docs/*.mdx`, then converted MDX → Markdown by a Node `remark-mdx` pipeline
- **Pi** — sourced from `github.com/earendil-works/pi` via `git sparse-checkout` on `packages/coding-agent/docs/*.md` (already clean Markdown)

CI re-fetches every 3 hours (GitHub Actions) and commits to `docs/`. Users
`git pull`, index the five `docs/<docset>/` folders in Miyo, and install a small
skill per agent. There is **no global installer and no background daemon** — the
old macOS `install.sh` / launchd model was removed.

## Docset layout — nested, mirroring the source's own categories

**Cursor is the first docset on the new nested layout** and the template the
others migrate to. Instead of flattening every page into one folder with `__`
path separators (the legacy scheme still used by claude-code/codex/opencode/pi),
the fetcher mirrors the source site's own category hierarchy as real subfolders
under the docset root:

```
docs/cursor/index.md                  ← cursor.com/docs.md (root page)
docs/cursor/agent/overview.md         ← cursor.com/docs/agent/overview.md
docs/cursor/agent/tools/terminal.md   ← cursor.com/docs/agent/tools/terminal.md
docs/cursor/models/gpt-5-5.md         ← cursor.com/docs/models/gpt-5-5.md
```

The leading `docs/` URL segment is dropped so categories sit at the docset root.
`docs_manifest.json` still lives at the docset root; its `files` keys are
POSIX-relative paths (`agent/overview.md`) rather than flat `agent__overview.md`.
The fetcher prunes empty category directories on cleanup.

## Toolchain — mise is the source of truth

Every tool, dependency, and task is declared in [`mise.toml`](mise.toml). Never
`pip install` / `npm install -g` by hand — add it to `mise.toml` and run
`mise install`. Entering the repo (`cd` in under `mise activate`) installs the
toolchain + deps and wires the local git hooks.

- **Tools** (`[tools]`): python, uv, node, ruff, hk, pkl (pinned; exact for
  runtimes, `latest` for CLIs — [`mise.lock`](mise.lock) records exact versions).
- **Deps** (`[deps.*]`): `uv pip install -r scripts/requirements.txt` and
  `npm ci` in `scripts/`, blake3 freshness-checked.
- **Tasks**: aggregates (`fetch`, `check`, `ci`, `setup`) live in `mise.toml`;
  leaf tasks live as auto-discovered file-tasks in [`.mise/tasks/`](.mise/tasks/)
  (`render`, `fmt`, `lint/python`, `fetch/{claude,codex,opencode,pi}`).

```bash
mise run fetch        # re-fetch all four docsets
mise run render       # templates → skills/<docset>/SKILL.md
mise run check        # ruff lint + ruff format-check + render-check
mise run ci           # render + check
```

Git hooks ([`hk.pkl`](hk.pkl)): pre-commit runs safety builtins + `mise run check`.
`docs/**` is excluded from the whitespace/newline auto-fixers (it is a verbatim
upstream mirror). Hooks install on **local** repo entry only, never in CI, so the
docs-bot's hourly auto-commits to `main` stay ungated. Line endings are LF
everywhere ([`.gitattributes`](.gitattributes)).

## Repo layout

```
agent-harness-docs/
├── docs/                              # mirrored docs (CI-updated) — index these in Miyo
│   ├── claude-code/   ~150 .md + docs_manifest.json   (flat, __ separators)
│   ├── codex/         ~90  .md + docs_manifest.json   (flat, __ separators)
│   ├── cursor/        ~180 .md + docs_manifest.json   (NESTED by category)
│   ├── opencode/      ~35  .md + docs_manifest.json   (flat, __ separators)
│   └── pi/            ~27  .md + docs_manifest.json   (flat, __ separators)
├── skills/
│   ├── templates/                     # Jinja2 source of truth
│   │   └── <docset>.SKILL.md.j2
│   └── <docset>/SKILL.md              # rendered, ONE per docset (Miyo-only)
├── scripts/
│   ├── fetch_claude_docs.py           → docs/claude-code/
│   ├── fetch_codex_docs.py            → docs/codex/
│   ├── fetch_cursor_docs.py           → docs/cursor/   (nested layout)
│   ├── fetch_opencode_docs.py         → docs/opencode/
│   ├── fetch_pi_docs.py               → docs/pi/
│   ├── mdx_to_md.mjs                  # Node MDX → MD (used by opencode fetcher)
│   ├── render_skills.py               # templates → skills/<docset>/SKILL.md
│   ├── requirements.txt  package.json  package-lock.json
├── mise.toml  mise.lock               # toolchain + deps + tasks
├── .mise/tasks/                       # leaf file-tasks
├── hk.pkl                             # git hooks
├── ruff.toml  .editorconfig  .flake8  .gitattributes
└── .github/workflows/update-docs.yml  # CI: fetch + commit every 3h
```

## How users consume this repo

1. `git pull` to get fresh `docs/`.
2. Index each `docs/<docset>/` folder in Miyo with the label `claude-code`,
   `codex`, `cursor`, `opencode`, or `pi`.
3. Install the skill for each agent with the [`skills`](https://skills.sh) CLI —
   **one skill per matching agent** (Claude Code doesn't need Codex docs):

   ```bash
   npx skills add mrkhachaturov/agent-harness-docs -g -a claude-code --skill claude-code-docs
   npx skills add mrkhachaturov/agent-harness-docs -g -a codex        --skill codex-docs
   npx skills add mrkhachaturov/agent-harness-docs -g -a cursor       --skill cursor-docs
   npx skills add mrkhachaturov/agent-harness-docs -g -a opencode     --skill opencode-docs
   npx skills add mrkhachaturov/agent-harness-docs -g -a pi           --skill pi-docs
   ```

   `npx skills add . …` installs from a local clone without a push. Skills are
   `disable-model-invocation: true` (manual-only, zero idle context) and invoked
   with `/<name>`.

## Four source-fetching patterns

| Source | Discovery | Per-page URL or method |
|---|---|---|
| Claude Code | `https://code.claude.com/docs/sitemap.xml` | `<page-url>.md` |
| Codex | `https://developers.openai.com/codex/llms.txt` (markdown list) | `https://developers.openai.com/codex/<slug>.md` |
| Cursor | `https://cursor.com/llms.txt` (markdown list, at site **root** not `/docs`) | `https://cursor.com/docs/<path>.md` — nested into `docs/cursor/<path>` |
| OpenCode | `git ls-remote` for default branch on `anomalyco/opencode` | `git sparse-checkout` of `/packages/web/src/content/docs/*.mdx` (non-cone), then `mdx_to_md.mjs` |
| Pi | `git ls-remote` for default branch on `earendil-works/pi` | `git sparse-checkout` of `/packages/coding-agent/docs/*.md` (non-cone), direct copy |

Cursor's `llms.txt` ships one malformed entry (`https://cursor.comhttps://cursor.com/changelog.md`,
duplicated prefix); the fetcher collapses `cursor.comhttps://cursor.com` → `cursor.com`
before extracting URLs. Unlike Codex, Cursor does **not** gate on `sec-ch-ua` /
`sec-fetch` headers — a plain UA suffices.

Codex pages 403 against bare `curl` — the fetcher sends the full Chrome header
set (`sec-ch-ua`, `sec-ch-ua-mobile`, `sec-ch-ua-platform`, `sec-fetch-*`);
without those Vercel returns "deny". TLS fingerprint is not checked, just headers.

OpenCode uses Astro Starlight MDX with `import` / `export` statements and JSX
components (`<Tabs>`, `<TabItem>`, `<Card>`, …). The MDX→MD pipeline
([`scripts/mdx_to_md.mjs`](scripts/mdx_to_md.mjs)) strips imports, unwraps JSX
(keeping children), and emits clean Markdown. Frontmatter, fenced code, lists,
tables, and Starlight directive callouts (`:::tip`, `:::note`) are preserved.

Pi docs are already clean Markdown — no conversion needed.

## Skills

One skill per docset, rendered to `skills/<docset>/SKILL.md`. Each skill:

- addresses its docs **only through the Miyo folder label** (`claude-code`,
  `codex`, `opencode`, `pi`) — no hardcoded filesystem path, so it is portable
  across macOS / Linux / Windows;
- carries `disable-model-invocation: true` — manual-only, zero idle context,
  invoked with `/<name>`;
- follows the same shape: portable-access note, a "how Miyo retrieval works
  (build better queries)" section, whole-docset + `path`-scoped search,
  when-to-read-the-full-file, anti-patterns, and `/<name>` sub-commands.

Install each to its **own** agent (`-a claude-code` / `-a codex` / `-a opencode`
/ `-a pi`); cross-install only when deliberately useful. The `skills` CLI places
each agent's skill in that agent's conventional directory automatically.

## Skill rendering

Skills are written once in
[`skills/templates/<docset>.SKILL.md.j2`](skills/templates/) and rendered to
`skills/<docset>/SKILL.md` by
[`scripts/render_skills.py`](scripts/render_skills.py) (`mise run render`). The
rendered files are committed; `mise run check` runs `render --check` to guard
against template/output drift. There are no per-indexer variants — the skills are
Miyo-only.

## MDX→MD conversion

The OpenCode fetcher is the only one that needs Node — for MDX parsing. The Node
side is isolated under `scripts/`:

- `scripts/package.json` lists deps (`unified`, `remark-parse`, `remark-mdx`,
  `remark-gfm`, `remark-stringify`, `unist-util-visit`, `mdast-util-to-string`)
- `scripts/package-lock.json` is committed so installs reproduce exactly
- `mise run deps` runs `npm ci` inside `scripts/`
- `scripts/mdx_to_md.mjs` reads MDX from stdin, emits Markdown on stdout
- `fetch_opencode_docs.py` calls `node scripts/mdx_to_md.mjs` per file

## Key files

- [`mise.toml`](mise.toml) — toolchain, deps, task aggregates
- [`.mise/tasks/`](.mise/tasks/) — leaf file-tasks
- [`hk.pkl`](hk.pkl) — git hooks
- [`scripts/fetch_claude_docs.py`](scripts/fetch_claude_docs.py), [`fetch_codex_docs.py`](scripts/fetch_codex_docs.py), [`fetch_cursor_docs.py`](scripts/fetch_cursor_docs.py), [`fetch_opencode_docs.py`](scripts/fetch_opencode_docs.py), [`fetch_pi_docs.py`](scripts/fetch_pi_docs.py)
- [`scripts/mdx_to_md.mjs`](scripts/mdx_to_md.mjs), [`scripts/render_skills.py`](scripts/render_skills.py)
- [`skills/templates/`](skills/templates/) — the four `.SKILL.md.j2` templates
- [`.github/workflows/update-docs.yml`](.github/workflows/update-docs.yml)
