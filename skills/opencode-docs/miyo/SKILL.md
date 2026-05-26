---
name: opencode-docs
description: Look up OpenCode documentation in the local mirror at ~/opencode-docs/. Use when answering questions about the OpenCode terminal UI, the `opencode` CLI, agents and subagents, opencode.json / opencode.jsonc config, skills, custom tools, plugins, MCP servers, providers and models, permissions, keybinds, themes, the SDK, share links, IDE integrations, GitHub/GitLab actions, ACP, or the LSP integration.
---

# OpenCode Documentation (local mirror)

The official OpenCode docs are mirrored at `~/opencode-docs/` — a flat folder
with ~34 `.md` files, auto-synced hourly from
`github.com/anomalyco/opencode` (`packages/web/src/content/docs/*.mdx`,
converted from MDX to plain Markdown).

## How to look up answers

Use Miyo MCP semantic search, scoped to this folder:

```
mcp__miyo__search(
  query: "<natural-language question>",
  folder_path: "opencode-docs",
  limit: 5            # 3–8 is usually enough; raise for broad topics
)
```

The tool returns ranked chunks with file paths and the snippet that matched.
For most questions the snippets answer directly — synthesize an answer and
cite source files inline as `[filename.md](~/opencode-docs/<filename>.md)`.

## When to read the full file

Fetch the raw file when the search chunk does not contain the exact detail
needed — typical reasons:

- exact JSON schema for `opencode.json` / `opencode.jsonc`
- full keybinds table or theme key list
- precise CLI flag spelling or full slash-command catalog
- complete list of skill / agent / MCP frontmatter fields and validation rules

To read the raw file, use the standard read tooling with the absolute path:

```
Read("/Users/<you>/opencode-docs/<filename>.md")
```

Miyo returns paths like `opencode-docs/<filename>.md` — drop the
`opencode-docs/` prefix and prepend `~/opencode-docs/`.

Do **not** use `mcp__miyo__read_file` for large docs — it returns the whole
file as one blob and gets truncated by the harness. Use Read with
`offset`/`limit` for surgical section reads instead.

## File naming

Filenames mirror the upstream slugs at
`packages/web/src/content/docs/`, with the `.mdx` extension replaced by
`.md`:

- `index.mdx` → `index.md` (the intro / getting-started page)
- `agents.mdx` → `agents.md`
- `mcp-servers.mdx` → `mcp-servers.md`
- `config.mdx` → `config.md`
- `skills.mdx` → `skills.md`

No subdirectories — the mirror is flat.

## What was stripped during MDX → Markdown conversion

The fetcher pipes each `.mdx` through a remark-mdx pipeline that:

- removes top-level `import` / `export` statements
- unwraps Astro Starlight components (`<Tabs>` / `<TabItem>` become bold
  section labels followed by their content; other JSX wrappers are
  unwrapped, keeping their children)
- preserves all standard Markdown (headings, lists, code, links, tables)
  and Starlight `:::tip` / `:::note` directives

So the local copy is highly readable, but a handful of UI-only details
(visual tab styling, icon names on `<Card>` components) are lost. If a
question depends on a missing visual element, fall back to the upstream
URL in the manifest entry's `upstream_url`.

## Anti-patterns

- Do **not** call `mcp__miyo__search` without `folder_path: "opencode-docs"`
  — results will leak from other indexed folders.
- Do **not** read raw docs first to "find" something — search first, read
  only when search results lack a specific detail.
- Do **not** use a web fetcher against `opencode.ai/docs/` or
  `github.com/anomalyco/opencode/` — the local mirror is fresher (CI
  updates upstream every few hours; launchd syncs the local mirror hourly)
  and rate-limit-free.

## Sub-commands the user may invoke

### `/opencode-docs <question>`
Search Miyo with the question. Synthesize an answer from the top 3–5 chunks
and cite source files.
### `/opencode-docs explain "<concept>"`
Run a broader search (`limit: 10`), group hits by file, and explain the
concept covering: definition, configuration, related features, gotchas.
### `/opencode-docs path "<A>" "<B>"`
Two searches — one per concept — then explain how they relate based on
overlap and any cross-references in the matched chunks.
### `/opencode-docs` (no args)
List what's indexed (`ls ~/opencode-docs/`) and suggest the user phrase a
question.
