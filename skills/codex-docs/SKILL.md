---
name: codex-docs
description: Look up OpenAI Codex documentation in the local Miyo-indexed folder labeled `codex` (resolved at runtime via Miyo — no hardcoded filesystem path, works on macOS/Windows/Linux). Use when answering questions about the Codex CLI, Codex app, IDE extension, cloud threads, AGENTS.md, config.toml, MCP servers in Codex, skills, plugins, hooks, sandboxing, approvals, slash commands, the Codex SDK, app-server, or the Codex GitHub Action.
disable-model-invocation: true
---

# Codex Documentation (local Miyo mirror)

A local Markdown mirror of the official [OpenAI Codex docs](https://developers.openai.com/codex)
(~90 pages from `developers.openai.com/codex`), indexed in **Miyo** under the folder
label **`codex`**. The docs are in **English** — phrase Miyo queries in English for best
recall.

> This skill is **manual-only** (`disable-model-invocation: true`): nothing loads into
> context until you invoke it with `/codex-docs`. Drop a copy at
> `~/.claude/skills/codex-docs/SKILL.md` (or your harness's skills dir) for it to be
> available in every chat at zero idle context cost. Remove that frontmatter line in a
> project copy if you want the agent to auto-invoke it there.

## Access is portable — never hardcode a filesystem path

This skill addresses the docs **only through Miyo's folder label `codex`**, not through
any absolute path. Miyo resolves the physical location on whatever machine it runs
(macOS/Windows/Linux), so the skill is portable.

- **Verify the folder exists** (and confirm its exact label) with
  `mcp__miyo__list_folders` — you should see `codex (… files, ready)`. If on some machine
  it was indexed under a different label, use that label everywhere below.
- **All file paths are Miyo-relative**, of the form `codex/<file>.md` — exactly as
  returned by `mcp__miyo__search` / `mcp__miyo__list_files`. Pass those same relative
  paths straight to `mcp__miyo__read_file`; **do not** prepend a mirror root and **do
  not** use the native `Read` tool (that would need an OS-specific absolute path and
  break portability).

## File naming

The mirror is a **flat** folder. Nested doc URLs flatten with `__` as the separator:

- `developers.openai.com/codex/quickstart` → `codex/quickstart.md`
- `developers.openai.com/codex/app/automations` → `codex/app__automations.md`
- `developers.openai.com/codex/concepts/sandboxing` → `codex/concepts__sandboxing.md`

So a whole section shares a filename prefix — every app page is `app__*.md`, every CLI
page is `cli__*.md`.

## How Miyo retrieval works (build better queries)

Miyo search is **hybrid**: for every query it runs two retrievers and fuses them with
**RRF** (Reciprocal Rank Fusion), then applies a **literal-match boost** (an exact query
substring in the title, then in the body, is pushed up):

- **Dense (semantic)** — embeds the query, matches by meaning. Good on paraphrase, weak
  when your wording is far from the docs' actual terms.
- **BM25 (lexical)** — keyword match. Good on exact terms/jargon, blind to synonyms.

A hit must surface in **at least one** retriever's prefetch to appear at all — RRF only
ranks what was already pulled. So the usual failure is **recall, not ranking**: if
neither semantic nor keyword catches it, raising `limit` or reranking won't help.

Query rules that follow from this:

- **Use Codex's own vocabulary** ("sandbox_mode", "approval_policy", "config.toml",
  "AGENTS.md", "codex exec", "workspace-write") rather than a casual paraphrase — this
  feeds BM25 and aligns the dense vector simultaneously.
- **Name the exact term** you expect in the doc (a TOML key, CLI flag, approval mode) —
  the literal boost rewards an exact substring.
- **If the first query misses, reformulate** with different/added domain terms or fire
  2–3 variants; don't just bump `limit`.
- Do **not** prepend instruction-style prefixes (e.g. `Instruct: …`) — Miyo embeds the
  query text verbatim and symmetrically with documents, so that only adds noise.

## Search the whole docset

Use Miyo semantic search scoped to the folder:

```
mcp__miyo__search(
  query: "<natural-language question>",
  folder_path: "codex",
  limit: 5            # 3–8 is usually enough; raise for broad topics
)
```

## Search a specific topic

Add the `path` filter (case-insensitive **substring** on the result path) to narrow to
one topic. The corpus is flat, so `path` matches a **filename fragment** — use the slug
prefix, no slashes:

```
# Codex app pages only
mcp__miyo__search(query: "...", folder_path: "codex", path: "app", limit: 5)

# CLI pages
mcp__miyo__search(query: "...", folder_path: "codex", path: "cli", limit: 5)

# Config pages
mcp__miyo__search(query: "...", folder_path: "codex", path: "config", limit: 5)
```

⚠️ **`path` must be a single fragment with no slash.** Miyo stores the folder prefix with
the OS-native separator (`\` on Windows, `/` on macOS/Linux), so a filter containing a
separator silently matches nothing on the wrong OS. Match the filename slug alone (e.g.
`path: "sandbox"`, `path: "mcp"`).

Miyo returns ranked chunks with file paths and the matched snippet. For most questions
the snippets answer directly — synthesize and cite source files inline by their
Miyo-relative path, e.g. `[config-basic.md](codex/config-basic.md)`.

## When to read the full file

Fetch the raw file when the search chunk lacks the exact detail — a full `config.toml`
key list, exact TOML schema, precise CLI flag spelling, or the complete catalog of slash
commands / approval modes.

Pass the **Miyo-relative path** that search/`list_files` returned straight to
`mcp__miyo__read_file` — no path rewriting, fully portable:

```
mcp__miyo__read_file(file_path: "codex/<file>.md")
```

If a page is large and `mcp__miyo__read_file` gets truncated by the harness, lean on the
search chunks (raise `limit`, or add a `path` filter) to pull just the relevant sections.

## Anti-patterns

- Do **not** call `mcp__miyo__search` without `folder_path: "codex"` — results will leak
  in from other indexed folders.
- Do **not** read raw docs first to "find" something — search first, read only when a
  chunk lacks a specific detail.
- Do **not** use a web fetcher against `developers.openai.com/codex/` — the local mirror
  is fresher and avoids Vercel's bot-protection layer.

## Sub-commands the user may invoke

### `/codex-docs <question>`
Search the whole docset (`folder_path: "codex"`). Synthesize an answer from the top 3–5
chunks and cite source files.

### `/codex-docs <topic> "<question>"`
Search scoped to a `path` fragment — e.g. `app` → `path: "app"`, `cli` → `path: "cli"`,
`config` → `path: "config"` (single fragment, no slash).

### `/codex-docs explain "<concept>"`
Broader search (`limit: 10`), group hits by file, and explain the concept covering:
definition, configuration, related features, gotchas.

### `/codex-docs` (no args)
List what's indexed (`mcp__miyo__list_files(file_path: "codex/")`, or
`mcp__miyo__list_folders` for the count) and suggest the user phrase a question.
