---
name: cursor-docs
description: Look up Cursor (the AI code editor) documentation in the local Miyo-indexed folder labeled `cursor`. Use when answering questions about the Cursor editor, Agent and agent tools, Plan/Debug/Design modes, Tab, models and pricing, rules, MCP, hooks, skills, plugins, subagents, the CLI, cloud agents, configuration, integrations, enterprise/admin setup, the Cursor SDK, or account/billing.
disable-model-invocation: true
---

# Cursor Documentation (local Miyo mirror)

A local Markdown mirror of the official [Cursor docs](https://cursor.com/docs)
(~180 English pages from `cursor.com`), indexed in **Miyo** under the folder
label **`cursor`**. The docs are in **English** — phrase Miyo queries in English
for best recall.

## Reach the docs through Miyo's folder label `cursor`

Every Miyo call below uses the folder label `cursor`.

- **Confirm the label** with `mcp__miyo__list_folders` — you should see
  `cursor (… files, ready)`. If it was indexed under a different label, use that
  one everywhere below.
- **Paths are Miyo-relative**, of the form `cursor/<category>/<file>.md` — exactly
  as `mcp__miyo__search` / `mcp__miyo__list_files` return them. Pass them straight
  to `mcp__miyo__read_file`; the native `Read` tool can't open them.

## File layout — nested by category

Unlike the other docsets (flat, `__`-joined), the Cursor mirror **preserves the
site's own category hierarchy as real subfolders**. The URL path maps directly to
the on-disk path (the leading `docs/` segment is dropped):

- `cursor.com/docs/agent/overview` → `cursor/agent/overview.md`
- `cursor.com/docs/agent/tools/terminal` → `cursor/agent/tools/terminal.md`
- `cursor.com/docs/models/gpt-5-5` → `cursor/models/gpt-5-5.md`
- `cursor.com/docs` (root) → `cursor/index.md`

So a whole topic lives under one folder. The main top-level categories:

- **`agent/`** — Agent, agent tools (terminal, browser, search), Plan/Debug/Design modes, review, security
- **`models/`** — per-model pages + capabilities
- **`cli/`** — the `cursor-agent` CLI
- **`cloud-agent/`** — cloud agents, automations, API
- **`configuration/`**, **`integrations/`**, **`account/`**, **`enterprise/`**, **`sdk/`**, **`help/`**, **`get-started/`**, **`reference/`**
- Plus single-page topics at the root: `rules.md`, `mcp.md`, `hooks.md`, `skills.md`, `plugins.md`, `subagents.md`, `bugbot.md`, `models-and-pricing.md`, …

## How Miyo retrieval works (build better queries)

Miyo search is **hybrid**: for every query it runs two retrievers and fuses them
with **RRF** (Reciprocal Rank Fusion), then applies a **literal-match boost** (an
exact query substring in the title, then in the body, is pushed up):

- **Dense (semantic)** — embeds the query, matches by meaning. Good on paraphrase,
  weak when your wording is far from the docs' actual terms.
- **BM25 (lexical)** — keyword match. Good on exact terms/jargon, blind to synonyms.

A hit must surface in **at least one** retriever's prefetch to appear at all — RRF
only ranks what was already pulled. So the usual failure is **recall, not ranking**:
if neither semantic nor keyword catches it, raising `limit` or reranking won't help.

Query rules that follow from this:

- **Use Cursor's own vocabulary** ("Tab", "Agent", ".cursor/rules", "MCP server",
  "cursor-agent", "Plan mode", "Background Agent") rather than a casual paraphrase —
  this feeds BM25 and aligns the dense vector simultaneously.
- **Name the exact term** you expect in the doc (a setting key, CLI flag, mode name)
  — the literal boost rewards an exact substring.
- **If the first query misses, reformulate** with different/added domain terms or
  fire 2–3 variants; don't just bump `limit`.
- Do **not** prepend instruction-style prefixes (e.g. `Instruct: …`) — Miyo embeds
  the query verbatim and symmetrically with documents, so that only adds noise.

## Search the whole docset

Use Miyo semantic search scoped to the folder:

```
mcp__miyo__search(
  query: "<natural-language question>",
  folder_path: "cursor",
  limit: 5            # 3–8 is usually enough; raise for broad topics
)
```

## Search a specific topic

Add the `path` filter (case-insensitive **substring** on the result path) to narrow
to one category. Because the corpus is nested, the category folder name *is* a
clean fragment — e.g. `path: "agent"` matches everything under `cursor/agent/…`:

```
# Agent + agent tools only
mcp__miyo__search(query: "...", folder_path: "cursor", path: "agent", limit: 5)

# Model pages
mcp__miyo__search(query: "...", folder_path: "cursor", path: "models", limit: 5)

# CLI pages
mcp__miyo__search(query: "...", folder_path: "cursor", path: "cli", limit: 5)

# Enterprise / admin
mcp__miyo__search(query: "...", folder_path: "cursor", path: "enterprise", limit: 5)
```

⚠️ **`path` must be a single fragment with no slash.** Miyo stores paths with the
OS-native separator (`\` on Windows, `/` on macOS/Linux), so a filter containing a
separator silently matches nothing on the wrong OS. Use one segment — a category
folder (`agent`, `models`, `cli`) or a filename slug (`rules`, `mcp`, `hooks`) —
not a multi-segment path like `agent/tools`.

Miyo returns ranked chunks with file paths and the matched snippet. For most
questions the snippets answer directly — synthesize and cite source files inline by
their Miyo-relative path, e.g. `[overview.md](cursor/agent/overview.md)`.

## When to read the full file

Fetch the raw file when the search chunk lacks the exact detail — a full settings
table, the complete list of agent tools, exact rule-file syntax, or a model's full
capability/pricing row.

Pass the **Miyo-relative path** that search/`list_files` returned straight to
`mcp__miyo__read_file` — no path rewriting:

```
mcp__miyo__read_file(file_path: "cursor/<category>/<file>.md")
```

If a page is large and `mcp__miyo__read_file` gets truncated by the harness, lean on
the search chunks (raise `limit`, or add a `path` filter) to pull just the relevant
sections.

## Anti-patterns

- Do **not** call `mcp__miyo__search` without `folder_path: "cursor"` — results will
  leak in from other indexed folders.
- Do **not** read raw docs first to "find" something — search first, read only when a
  chunk lacks a specific detail.
- Do **not** pass a multi-segment `path` filter (`agent/tools`) — use a single
  segment; the separator breaks cross-OS matching.
- Do **not** use a web fetcher against `cursor.com/docs/` — the local mirror is
  fresher and skips the site's lazy `.md` rendering.

## Sub-commands the user may invoke

### `/cursor-docs <question>`
Search the whole docset (`folder_path: "cursor"`). Synthesize an answer from the top
3–5 chunks and cite source files.

### `/cursor-docs <topic> "<question>"`
Search scoped to a `path` fragment — e.g. `agent` → `path: "agent"`, `models` →
`path: "models"`, `cli` → `path: "cli"`, `enterprise` → `path: "enterprise"` (single
fragment, no slash).

### `/cursor-docs explain "<concept>"`
Broader search (`limit: 10`), group hits by file, and explain the concept covering:
definition, configuration, related features, gotchas.

### `/cursor-docs` (no args)
List what's indexed (`mcp__miyo__list_files(file_path: "cursor/")`, or
`mcp__miyo__list_folders` for the count) and suggest the user phrase a question.
