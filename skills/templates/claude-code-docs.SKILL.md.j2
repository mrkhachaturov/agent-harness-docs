---
name: claude-code-docs
description: Look up Claude Code documentation in the local Miyo-indexed folder labeled `claude-code`. Use when answering questions about Claude Code — features, configuration, hooks, permissions, settings, MCP, plugins, skills, sub-agents, Agent SDK, CLI flags, slash commands, env vars, cloud providers, or IDE integrations.
disable-model-invocation: true
---

# Claude Code Documentation (local Miyo mirror)

A local Markdown mirror of the official [Claude Code docs](https://code.claude.com/docs)
(~150 pages from `code.claude.com`, plus the release changelog), indexed in **Miyo**
under the folder label **`claude-code`**. The docs are in **English** — phrase Miyo
queries in English for best recall.

## Reach the docs through Miyo's folder label `claude-code`

Every Miyo call below uses the folder label `claude-code`.

- **Confirm the label** with `mcp__miyo__list_folders` — you should see
  `claude-code (… files, ready)`. If it was indexed under a different label, use that
  one everywhere below.
- **Paths are Miyo-relative**, of the form `claude-code/<file>.md` — exactly as
  `mcp__miyo__search` / `mcp__miyo__list_files` return them. Pass them straight to
  `mcp__miyo__read_file`; the native `Read` tool can't open them.

## File naming

The mirror is a **flat** folder. Nested doc URLs flatten with `__` as the separator:

- `code.claude.com/docs/en/hooks` → `claude-code/hooks.md`
- `code.claude.com/docs/en/agent-sdk/skills` → `claude-code/agent-sdk__skills.md`

So a whole topic family shares a filename prefix — every SDK page is `agent-sdk__*.md`.

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

- **Use Claude Code's own vocabulary** ("PreToolUse hook", "permission mode", "MCP
  server", "subagent", "settings.json", "output style") rather than a casual paraphrase —
  this feeds BM25 and aligns the dense vector simultaneously.
- **Name the exact term** you expect in the doc (a setting key, CLI flag, hook event,
  env var) — the literal boost rewards an exact substring.
- **If the first query misses, reformulate** with different/added domain terms or fire
  2–3 variants; don't just bump `limit`.
- Do **not** prepend instruction-style prefixes (e.g. `Instruct: …`) — Miyo embeds the
  query text verbatim and symmetrically with documents, so that only adds noise.

## Search the whole docset

Use Miyo semantic search scoped to the folder:

```
mcp__miyo__search(
  query: "<natural-language question>",
  folder_path: "claude-code",
  limit: 5            # 3–8 is usually enough; raise for broad topics
)
```

## Search a specific topic

Add the `path` filter (case-insensitive **substring** on the result path) to narrow to
one topic. The corpus is flat, so `path` matches a **filename fragment** — use the slug
prefix, no slashes:

```
# Agent SDK pages only
mcp__miyo__search(query: "...", folder_path: "claude-code", path: "agent-sdk", limit: 5)

# Hooks
mcp__miyo__search(query: "...", folder_path: "claude-code", path: "hooks", limit: 5)

# MCP
mcp__miyo__search(query: "...", folder_path: "claude-code", path: "mcp", limit: 5)
```

⚠️ **`path` must be a single fragment with no slash.** Miyo stores the folder prefix with
the OS-native separator (`\` on Windows, `/` on macOS/Linux), so a filter containing a
separator silently matches nothing on the wrong OS. Match the filename slug alone (e.g.
`path: "settings"`, `path: "permissions"`).

Miyo returns ranked chunks with file paths and the matched snippet. For most questions
the snippets answer directly — synthesize and cite source files inline by their
Miyo-relative path, e.g. `[hooks.md](claude-code/hooks.md)`.

## When to read the full file

Fetch the raw file when the search chunk lacks the exact detail — an exact JSON schema,
YAML frontmatter, precise CLI flag spelling, or a full env-var / settings / hook-event
reference table.

Pass the **Miyo-relative path** that search/`list_files` returned straight to
`mcp__miyo__read_file` — no path rewriting:

```
mcp__miyo__read_file(file_path: "claude-code/<file>.md")
```

Some Claude Code pages are large (the CLI, settings, and hooks references especially).
`mcp__miyo__read_file` returns the whole file as one blob and can be truncated by the
harness — if that happens, lean on the search chunks (raise `limit`, or add a `path`
filter) to pull just the relevant sections instead.

## Anti-patterns

- Do **not** call `mcp__miyo__search` without `folder_path: "claude-code"` — results
  will leak in from other indexed folders.
- Do **not** read raw docs first to "find" something — search first, read only when a
  chunk lacks a specific detail.
- Do **not** use `WebFetch` against `code.claude.com` — the local mirror is fresher and
  rate-limit-free.

## Sub-commands the user may invoke

### `/claude-code-docs <question>`
Search the whole docset (`folder_path: "claude-code"`). Synthesize an answer from the
top 3–5 chunks and cite source files.

### `/claude-code-docs <topic> "<question>"`
Search scoped to a `path` fragment — e.g. `sdk` → `path: "agent-sdk"`, `hooks` →
`path: "hooks"`, `mcp` → `path: "mcp"` (single fragment, no slash).

### `/claude-code-docs explain "<concept>"`
Broader search (`limit: 10`), group hits by file, and explain the concept covering:
definition, configuration, related features, gotchas.

### `/claude-code-docs` (no args)
List what's indexed (`mcp__miyo__list_files(file_path: "claude-code/")`, or
`mcp__miyo__list_folders` for the count) and suggest the user phrase a question.
