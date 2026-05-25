---
name: claude-code-docs
description: Look up Claude Code documentation in the local mirror at ~/claude-code-docs/. Use when answering questions about Claude Code features, configuration, hooks, permissions, settings, MCP, plugins, skills, sub-agents, Agent SDK, CLI flags, env vars, cloud providers, or IDE integrations.
---

# Claude Code Documentation (local mirror)

The official Claude Code docs are mirrored at `~/claude-code-docs/` — a flat
folder with ~140 `.md` files, auto-synced hourly from `code.claude.com`.

## How to look up answers

Use Miyo MCP semantic search, scoped to this folder:

```
mcp__miyo__search(
  query: "<natural-language question>",
  folder_path: "claude-code-docs",
  limit: 5            # 3–8 is usually enough; raise for broad topics
)
```

The tool returns ranked chunks with file paths and the snippet that matched.
For most questions the snippets answer directly — synthesize an answer and
cite source files inline as `[filename.md](~/claude-code-docs/<filename>.md)`.

## When to read the full file

Fetch the raw file when the search chunk does not contain the exact detail
needed — typical reasons:

- exact JSON schema, YAML frontmatter, or config example
- precise CLI flag spelling or option list
- the full table of an env-var / settings / hook event reference

To read the raw file, use the standard read tooling with the absolute path:

```
Read("/Users/<you>/claude-code-docs/<filename>.md")
```

Miyo returns paths like `claude-code-docs/<filename>.md` — drop the
`claude-code-docs/` prefix and prepend `~/claude-code-docs/`.

Do **not** use `mcp__miyo__read_file` for large docs — it returns the whole
file as one blob and gets truncated by the harness. Use Read with
`offset`/`limit` for surgical section reads instead.

## File naming

The mirror flattens the URL path with `__` as the separator:

- `code.claude.com/docs/en/hooks` → `hooks.md`
- `code.claude.com/docs/en/agent-sdk/skills` → `agent-sdk__skills.md`

## Anti-patterns

- Do **not** call `mcp__miyo__search` without `folder_path: "claude-code-docs"`
  — results will include unrelated indexed folders.
- Do **not** read raw docs first to "find" something — search first, read
  only when search results lack a specific detail.
- Do **not** use `WebFetch` against `code.claude.com` — the local mirror is
  fresher (CI updates upstream every few hours; launchd syncs the local
  mirror hourly) and avoids rate limits.

## Sub-commands the user may invoke

### `/claude-code-docs <question>`
Search Miyo with the question. Synthesize an answer from the top 3–5 chunks
and cite source files.
### `/claude-code-docs explain "<concept>"`
Run a broader search (`limit: 10`), group hits by file, and explain the
concept covering: definition, configuration, related features, gotchas.
### `/claude-code-docs path "<A>" "<B>"`
Two searches — one per concept — then explain how they relate based on
overlap and any cross-references in the matched chunks.
### `/claude-code-docs` (no args)
List what's indexed (`ls ~/claude-code-docs/`) and suggest the user phrase a
question.
