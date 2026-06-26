---
name: pi-docs
description: Look up Pi coding-agent documentation in the local Miyo-indexed folder labeled `pi`. Use when answering questions about the Pi terminal coding harness, the `pi` CLI, extensions, skills, prompt templates, themes, pi packages, providers, models, settings, keybindings, sessions, compaction, the Pi SDK, RPC mode, JSON event stream, or TUI components.
disable-model-invocation: true
---

# Pi Documentation (local Miyo mirror)

A local Markdown mirror of the official Pi coding-agent docs
(~27 pages from `github.com/earendil-works/pi`, `packages/coding-agent/docs/`), indexed
in **Miyo** under the folder label **`pi`**. The docs are in **English** — phrase Miyo
queries in English for best recall.

## Reach the docs through Miyo's folder label `pi`

Every Miyo call below uses the folder label `pi`.

- **Confirm the label** with `mcp__miyo__list_folders` — you should see
  `pi (… files, ready)`. If it was indexed under a different label, use that one
  everywhere below.
- **Paths are Miyo-relative**, of the form `pi/<file>.md` — exactly as
  `mcp__miyo__search` / `mcp__miyo__list_files` return them. Pass them straight to
  `mcp__miyo__read_file`; the native `Read` tool can't open them.

## File naming

Filenames match the upstream slugs at `packages/coding-agent/docs/` directly. The mirror
is **flat** — no subdirectories:

- `pi/index.md` (the overview / getting-started page)
- `pi/extensions.md`, `pi/skills.md`, `pi/sdk.md`
- `pi/keybindings.md`, `pi/models.md`, `pi/compaction.md`

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

- **Use Pi's own vocabulary** ("extension", "prompt template", "compaction", "RPC mode",
  "JSON event stream", "provider", "keybinding") rather than a casual paraphrase — this
  feeds BM25 and aligns the dense vector simultaneously.
- **Name the exact term** you expect in the doc (a setting, CLI flag, event name) — the
  literal boost rewards an exact substring.
- **If the first query misses, reformulate** with different/added domain terms or fire
  2–3 variants; don't just bump `limit`.
- Do **not** prepend instruction-style prefixes (e.g. `Instruct: …`) — Miyo embeds the
  query text verbatim and symmetrically with documents, so that only adds noise.

## Search the whole docset

Use Miyo semantic search scoped to the folder:

```
mcp__miyo__search(
  query: "<natural-language question>",
  folder_path: "pi",
  limit: 5            # 3–8 is usually enough; raise for broad topics
)
```

## Search a specific topic

Add the `path` filter (case-insensitive **substring** on the result path) to narrow to
one file. The corpus is flat, so `path` matches a **filename fragment**, no slashes:

```
# Extensions
mcp__miyo__search(query: "...", folder_path: "pi", path: "extensions", limit: 5)

# Sessions / compaction
mcp__miyo__search(query: "...", folder_path: "pi", path: "compaction", limit: 5)
```

⚠️ **`path` must be a single fragment with no slash.** Miyo stores the folder prefix with
the OS-native separator (`\` on Windows, `/` on macOS/Linux), so a filter containing a
separator silently matches nothing on the wrong OS. Match the filename slug alone.

Miyo returns ranked chunks with file paths and the matched snippet. For most questions
the snippets answer directly — synthesize and cite source files inline by their
Miyo-relative path, e.g. `[extensions.md](pi/extensions.md)`.

## When to read the full file

Fetch the raw file when the search chunk lacks the exact detail — an exact JSON schema
for settings or extension manifests, full keybindings/theme table, precise CLI flag
spelling, or the complete provider/model configuration reference.

Pass the **Miyo-relative path** that search/`list_files` returned straight to
`mcp__miyo__read_file` — no path rewriting:

```
mcp__miyo__read_file(file_path: "pi/<file>.md")
```

If a page is large and `mcp__miyo__read_file` gets truncated by the harness, lean on the
search chunks (raise `limit`, or add a `path` filter) to pull just the relevant sections.

## Anti-patterns

- Do **not** call `mcp__miyo__search` without `folder_path: "pi"` — results will leak in
  from other indexed folders.
- Do **not** read raw docs first to "find" something — search first, read only when a
  chunk lacks a specific detail.
- Do **not** use a web fetcher against `github.com/earendil-works/pi/` — the local mirror
  is fresher and rate-limit-free.

## Sub-commands the user may invoke

### `/pi-docs <question>`
Search the whole docset (`folder_path: "pi"`). Synthesize an answer from the top 3–5
chunks and cite source files.

### `/pi-docs <topic> "<question>"`
Search scoped to a `path` fragment — e.g. `extensions` → `path: "extensions"`,
`sessions` → `path: "sessions"` (single fragment, no slash).

### `/pi-docs explain "<concept>"`
Broader search (`limit: 10`), group hits by file, and explain the concept covering:
definition, configuration, related features, gotchas.

### `/pi-docs` (no args)
List what's indexed (`mcp__miyo__list_files(file_path: "pi/")`, or
`mcp__miyo__list_folders` for the count) and suggest the user phrase a question.
