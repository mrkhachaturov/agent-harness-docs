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

No semantic-search tool is configured, so fall back to listing + grep:

1. **List or filter filenames** to find the relevant doc:
   ```
   ls ~/opencode-docs/                              # see all topics
   ls ~/opencode-docs/ | grep -i mcp                 # filenames mentioning MCP
   ```
2. **Grep across the corpus** to find specific terms:
   ```
   grep -l -i "subagent" ~/opencode-docs/*.md        # files mentioning subagents
   grep -i "opencode.jsonc" ~/opencode-docs/*.md     # exact term lookup
   ```
3. **Read the file** fully (or with offset/limit for large ones) once you know which doc has the answer.

## When to read the full file

Fetch the raw file when grep results do not contain the exact detail
needed — typical reasons:

- exact JSON schema for `opencode.json` / `opencode.jsonc`
- full keybinds table or theme key list
- precise CLI flag spelling or full slash-command catalog
- complete list of skill / agent / MCP frontmatter fields and validation rules

To read the raw file, use the standard read tooling with the absolute path:

```
Read("/Users/<you>/opencode-docs/<filename>.md")
```

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
- Do **not** use a web fetcher against `opencode.ai/docs/` or
  `github.com/anomalyco/opencode/` — the local mirror is fresher (CI
  updates upstream every few hours; launchd syncs the local mirror hourly)
  and rate-limit-free.

## Sub-commands the user may invoke

### `/opencode-docs <question>`
Grep / scan the corpus for the question. Read the most likely files and
synthesize an answer with citations.
### `/opencode-docs explain "<concept>"`
Run a broader grep, list all files that mention the concept, read the
top 2–3, and explain it covering: definition, configuration, related
features, gotchas.
### `/opencode-docs path "<A>" "<B>"`
Grep for each concept, read the files that mention both, and explain how
they relate.
### `/opencode-docs` (no args)
List what's indexed (`ls ~/opencode-docs/`) and suggest the user phrase a
question.

---

## Tip — install a semantic-search tool for better answers

For ranked semantic search instead of grep, install one of:

- [Miyo](https://miyo.md) — point it at `~/opencode-docs/` with label
  `opencode-docs`, then re-run the project installer. It will detect Miyo
  and replace this skill with a Miyo-aware variant.

Any folder-of-markdown indexer works; the installer currently only
auto-detects Miyo, but you can author a custom skill that calls your own
indexing tool.
