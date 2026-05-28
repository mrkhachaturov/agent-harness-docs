---
name: pi-docs
description: Look up Pi coding-agent documentation in the local mirror at ~/pi-docs/. Use when answering questions about the Pi terminal coding harness, the `pi` CLI, extensions, skills, prompt templates, themes, pi packages, providers, models, settings, keybindings, sessions, compaction, the Pi SDK, RPC mode, JSON event stream, or TUI components.
---

# Pi Documentation (local mirror)

The official Pi docs are mirrored at `~/pi-docs/` — a flat folder
with ~27 `.md` files, auto-synced hourly from
`github.com/earendil-works/pi` (`packages/coding-agent/docs/*.md`).

## How to look up answers

Use Miyo MCP semantic search, scoped to this folder:

```
mcp__miyo__search(
  query: "<natural-language question>",
  folder_path: "pi-docs",
  limit: 5            # 3–8 is usually enough; raise for broad topics
)
```

The tool returns ranked chunks with file paths and the snippet that matched.
For most questions the snippets answer directly — synthesize an answer and
cite source files inline as `[filename.md](~/pi-docs/<filename>.md)`.

## When to read the full file

Fetch the raw file when the search chunk does not contain the exact detail
needed — typical reasons:

- exact JSON schema for settings or extension manifests
- full keybindings table or theme key list
- precise CLI flag spelling or full slash-command catalog
- complete provider / model configuration reference

To read the raw file, use the standard read tooling with the absolute path:

```
Read("/Users/<you>/pi-docs/<filename>.md")
```

Miyo returns paths like `pi-docs/<filename>.md` — drop the `pi-docs/`
prefix and prepend `~/pi-docs/`.

Do **not** use `mcp__miyo__read_file` for large docs — it returns the whole
file as one blob and gets truncated by the harness. Use Read with
`offset`/`limit` for surgical section reads instead.

## File naming

Filenames match the upstream slugs at
`packages/coding-agent/docs/` directly:

- `index.md` (the overview / getting-started page)
- `quickstart.md`, `usage.md`, `providers.md`
- `extensions.md`, `skills.md`, `sdk.md`
- `sessions.md`, `session-format.md`

No subdirectories — the mirror is flat.

## Anti-patterns

- Do **not** call `mcp__miyo__search` without `folder_path: "pi-docs"`
  — results will leak from other indexed folders.
- Do **not** read raw docs first to "find" something — search first, read
  only when search results lack a specific detail.
- Do **not** use a web fetcher against `github.com/earendil-works/pi/` —
  the local mirror is fresher (CI updates upstream every few hours; launchd
  syncs the local mirror hourly) and rate-limit-free.

## Sub-commands the user may invoke

### `/pi-docs <question>`
Search Miyo with the question. Synthesize an answer from the top 3–5 chunks
and cite source files.
### `/pi-docs explain "<concept>"`
Run a broader search (`limit: 10`), group hits by file, and explain the
concept covering: definition, configuration, related features, gotchas.
### `/pi-docs path "<A>" "<B>"`
Two searches — one per concept — then explain how they relate based on
overlap and any cross-references in the matched chunks.
### `/pi-docs` (no args)
List what's indexed (`ls ~/pi-docs/`) and suggest the user phrase a
question.
