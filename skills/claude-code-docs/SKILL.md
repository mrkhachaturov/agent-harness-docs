---
name: claude-code-docs
description: Search the Claude Code documentation via Miyo (local semantic search). Use when asked about Claude Code features, configuration, hooks, permissions, settings, MCP, plugins, skills, sub-agents, Agent SDK, CLI flags, env vars, cloud providers, or IDE integrations.
when_to_use: Any question about how Claude Code works, how to configure it, or what features exist. Prefer over WebFetch against docs.anthropic.com — the local index is fresher and rate-limit-free.
disable-model-invocation: false
---

# Claude Code Documentation

Semantic search over the official Claude Code documentation via Miyo
(local Jina v5 Nano embeddings + reranking). The corpus is the
`claude-code-docs` folder indexed in Miyo — point Miyo at
`~/claude-code-docs/` (the docs are flat in that directory; a launchd
job keeps the folder in sync with the upstream git repo every hour).

## How to query

Always call `mcp__miyo__search` with `folder_path: "claude-code-docs"` so
results stay scoped to the Claude Code docs and do not leak from other
indexed folders.

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

Fetch the raw file only if the chunk does not contain the exact detail
needed — typical reasons:

- exact JSON schema, YAML frontmatter, or config example
- precise CLI flag spelling or option list
- the full table of an env-var / settings / hook event reference

To read the raw file, use the **Read** tool with the absolute path:

```
Read("/Users/<you>/claude-code-docs/<filename>.md")
```

Miyo returns paths like `claude-code-docs/<filename>.md` — drop the
`claude-code-docs/` prefix and prepend `~/claude-code-docs/`.

Do **not** use `mcp__miyo__read_file` for large docs — it returns the whole
file as one blob and gets truncated by the harness. Use Read with
`offset`/`limit` for surgical section reads instead.

## Anti-patterns

- Do **not** call `mcp__miyo__search` without `folder_path: "claude-code-docs"`
  — results will include unrelated indexed folders.
- Do **not** read raw docs first to "find" something — search first, read
  only when search results lack a specific detail.
- Do **not** use `WebFetch` against `docs.anthropic.com` — the local index
  is fresher (CI updates upstream every few hours; launchd syncs the local
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
Show what's indexed:
```
mcp__miyo__list_files(file_path: "claude-code-docs/", limit: 200)
```
List the topics and suggest the user phrase a question.
