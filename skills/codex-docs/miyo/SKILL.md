---
name: codex-docs
description: Look up OpenAI Codex documentation in the local mirror at ~/codex-docs/. Use when answering questions about the Codex CLI, Codex app, IDE extension, cloud threads, AGENTS.md, config.toml, MCP servers in Codex, skills, plugins, hooks, sandboxing, approvals, slash commands, the Codex SDK, app-server, or the Codex GitHub Action.
---

# Codex Documentation (local mirror)

The official Codex docs are mirrored at `~/codex-docs/` — a flat folder
with ~80 `.md` files, auto-synced hourly from `developers.openai.com/codex`.

## How to look up answers

Use Miyo MCP semantic search, scoped to this folder:

```
mcp__miyo__search(
  query: "<natural-language question>",
  folder_path: "codex-docs",
  limit: 5            # 3–8 is usually enough; raise for broad topics
)
```

The tool returns ranked chunks with file paths and the snippet that matched.
For most questions the snippets answer directly — synthesize an answer and
cite source files inline as `[filename.md](~/codex-docs/<filename>.md)`.

## When to read the full file

Fetch the raw file when the search chunk does not contain the exact detail
needed — typical reasons:

- exact TOML schema or full `config.toml` key list
- precise CLI flag spelling or option list
- the full table of an env-var / settings / hook event reference
- the complete catalog of slash commands

To read the raw file, use the standard read tooling with the absolute path:

```
Read("/Users/<you>/codex-docs/<filename>.md")
```

Miyo returns paths like `codex-docs/<filename>.md` — drop the `codex-docs/`
prefix and prepend `~/codex-docs/`.

Do **not** use `mcp__miyo__read_file` for large docs — it returns the whole
file as one blob and gets truncated by the harness. Use Read with
`offset`/`limit` for surgical section reads instead.

## File naming

The mirror flattens the URL path with `__` as the separator:

- `developers.openai.com/codex/quickstart` → `quickstart.md`
- `developers.openai.com/codex/app/automations` → `app__automations.md`
- `developers.openai.com/codex/concepts/sandboxing` → `concepts__sandboxing.md`

## Anti-patterns

- Do **not** call `mcp__miyo__search` without `folder_path: "codex-docs"`
  — results will include unrelated indexed folders.
- Do **not** read raw docs first to "find" something — search first, read
  only when search results lack a specific detail.
- Do **not** use a web fetcher against `developers.openai.com/codex/` — the
  local mirror is fresher (CI updates upstream every few hours; launchd
  syncs the local mirror hourly) and avoids Vercel's bot-protection layer.

## Sub-commands the user may invoke

### `/codex-docs <question>`
Search Miyo with the question. Synthesize an answer from the top 3–5 chunks
and cite source files.
### `/codex-docs explain "<concept>"`
Run a broader search (`limit: 10`), group hits by file, and explain the
concept covering: definition, configuration, related features, gotchas.
### `/codex-docs path "<A>" "<B>"`
Two searches — one per concept — then explain how they relate based on
overlap and any cross-references in the matched chunks.
### `/codex-docs` (no args)
List what's indexed (`ls ~/codex-docs/`) and suggest the user phrase a
question.
