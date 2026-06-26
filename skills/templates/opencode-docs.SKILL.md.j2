---
name: opencode-docs
description: Look up OpenCode documentation in the local Miyo-indexed folder labeled `opencode`. Use when answering questions about the OpenCode terminal UI, the `opencode` CLI, agents and subagents, opencode.json / opencode.jsonc config, skills, custom tools, plugins, MCP servers, providers and models, permissions, keybinds, themes, the SDK, share links, IDE integrations, GitHub/GitLab actions, ACP, or the LSP integration.
disable-model-invocation: true
---

# OpenCode Documentation (local Miyo mirror)

A local Markdown mirror of the official [OpenCode docs](https://opencode.ai/docs)
(~35 pages from `github.com/anomalyco/opencode`, converted from MDX to plain Markdown),
indexed in **Miyo** under the folder label **`opencode`**. The docs are in **English** —
phrase Miyo queries in English for best recall.

## Reach the docs through Miyo's folder label `opencode`

Every Miyo call below uses the folder label `opencode`.

- **Confirm the label** with `mcp__miyo__list_folders` — you should see
  `opencode (… files, ready)`. If it was indexed under a different label, use that
  one everywhere below.
- **Paths are Miyo-relative**, of the form `opencode/<file>.md` — exactly as
  `mcp__miyo__search` / `mcp__miyo__list_files` return them. Pass them straight to
  `mcp__miyo__read_file`; the native `Read` tool can't open them.

## File naming

Filenames mirror the upstream slugs at `packages/web/src/content/docs/`, with `.mdx`
replaced by `.md`. The mirror is **flat** — no subdirectories:

- `index.mdx` → `opencode/index.md` (the intro / getting-started page)
- `agents.mdx` → `opencode/agents.md`
- `config.mdx` → `opencode/config.md`
- `mcp-servers.mdx` → `opencode/mcp-servers.md`

## What was stripped during MDX → Markdown conversion

The fetcher pipes each `.mdx` through a remark-mdx pipeline that removes `import`/`export`
statements and unwraps Astro Starlight components (`<Tabs>` / `<TabItem>` become bold
section labels followed by their content; other JSX wrappers are unwrapped, keeping their
children). All standard Markdown and `:::tip` / `:::note` directives are preserved. A few
UI-only details (tab styling, `<Card>` icon names) are lost — if a question depends on a
missing visual element, fall back to the upstream URL in the manifest entry.

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

- **Use OpenCode's own vocabulary** ("opencode.json", "subagent", "permission", "primary
  agent", "MCP server", "keybind", "provider") rather than a casual paraphrase — this
  feeds BM25 and aligns the dense vector simultaneously.
- **Name the exact term** you expect in the doc (a config key, permission key, CLI flag) —
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
  folder_path: "opencode",
  limit: 5            # 3–8 is usually enough; raise for broad topics
)
```

## Search a specific topic

Add the `path` filter (case-insensitive **substring** on the result path) to narrow to
one file. The corpus is flat, so `path` matches a **filename fragment**, no slashes:

```
# Agents / subagents
mcp__miyo__search(query: "...", folder_path: "opencode", path: "agents", limit: 5)

# Config
mcp__miyo__search(query: "...", folder_path: "opencode", path: "config", limit: 5)
```

⚠️ **`path` must be a single fragment with no slash.** Miyo stores the folder prefix with
the OS-native separator (`\` on Windows, `/` on macOS/Linux), so a filter containing a
separator silently matches nothing on the wrong OS. Match the filename slug alone.

Miyo returns ranked chunks with file paths and the matched snippet. For most questions
the snippets answer directly — synthesize and cite source files inline by their
Miyo-relative path, e.g. `[agents.md](opencode/agents.md)`.

## When to read the full file

Fetch the raw file when the search chunk lacks the exact detail — an exact JSON schema
for `opencode.json`, full keybinds/theme table, precise CLI flag spelling, or the
complete list of agent/skill/MCP frontmatter fields.

Pass the **Miyo-relative path** that search/`list_files` returned straight to
`mcp__miyo__read_file` — no path rewriting:

```
mcp__miyo__read_file(file_path: "opencode/<file>.md")
```

If a page is large and `mcp__miyo__read_file` gets truncated by the harness, lean on the
search chunks (raise `limit`, or add a `path` filter) to pull just the relevant sections.

## Anti-patterns

- Do **not** call `mcp__miyo__search` without `folder_path: "opencode"` — results will
  leak in from other indexed folders.
- Do **not** read raw docs first to "find" something — search first, read only when a
  chunk lacks a specific detail.
- Do **not** use a web fetcher against `opencode.ai/docs/` or
  `github.com/anomalyco/opencode/` — the local mirror is fresher and rate-limit-free.

## Sub-commands the user may invoke

### `/opencode-docs <question>`
Search the whole docset (`folder_path: "opencode"`). Synthesize an answer from the top
3–5 chunks and cite source files.

### `/opencode-docs <topic> "<question>"`
Search scoped to a `path` fragment — e.g. `agents` → `path: "agents"`, `config` →
`path: "config"` (single fragment, no slash).

### `/opencode-docs explain "<concept>"`
Broader search (`limit: 10`), group hits by file, and explain the concept covering:
definition, configuration, related features, gotchas.

### `/opencode-docs` (no args)
List what's indexed (`mcp__miyo__list_files(file_path: "opencode/")`, or
`mcp__miyo__list_folders` for the count) and suggest the user phrase a question.
