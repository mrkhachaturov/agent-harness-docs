---
name: claude-code-docs
description: Look up Claude Code documentation in the local mirror at ~/claude-code-docs/. Use when answering questions about Claude Code features, configuration, hooks, permissions, settings, MCP, plugins, skills, sub-agents, Agent SDK, CLI flags, env vars, cloud providers, or IDE integrations.
---

# Claude Code Documentation (local mirror)

The official Claude Code docs are mirrored at `~/claude-code-docs/` — a flat
folder with ~140 `.md` files, auto-synced hourly from `code.claude.com`.

## How to look up answers

No semantic-search tool is configured, so fall back to listing + grep:

1. **List or filter filenames** to find the relevant doc:
   ```
   ls ~/claude-code-docs/                          # see all topics
   ls ~/claude-code-docs/ | grep -i hook            # filenames mentioning hooks
   ```
2. **Grep across the corpus** to find specific terms:
   ```
   grep -l -i "hook" ~/claude-code-docs/*.md        # files containing "hook"
   grep -i "preToolUse" ~/claude-code-docs/*.md     # exact term lookup
   ```
3. **Read the file** fully (or with offset/limit for large ones) once you know which doc has the answer.

## When to read the full file

Fetch the raw file when grep results do not contain the exact detail
needed — typical reasons:

- exact JSON schema, YAML frontmatter, or config example
- precise CLI flag spelling or option list
- the full table of an env-var / settings / hook event reference

To read the raw file, use the standard read tooling with the absolute path:

```
Read("/Users/<you>/claude-code-docs/<filename>.md")
```

## File naming

The mirror flattens the URL path with `__` as the separator:

- `code.claude.com/docs/en/hooks` → `hooks.md`
- `code.claude.com/docs/en/agent-sdk/skills` → `agent-sdk__skills.md`

## Anti-patterns
- Do **not** use `WebFetch` against `code.claude.com` — the local mirror is
  fresher (CI updates upstream every few hours; launchd syncs the local
  mirror hourly) and avoids rate limits.

## Sub-commands the user may invoke

### `/claude-code-docs <question>`
Grep / scan the corpus for the question. Read the most likely files and
synthesize an answer with citations.
### `/claude-code-docs explain "<concept>"`
Run a broader grep, list all files that mention the concept, read the
top 2–3, and explain it covering: definition, configuration, related
features, gotchas.
### `/claude-code-docs path "<A>" "<B>"`
Grep for each concept, read the files that mention both, and explain how
they relate.
### `/claude-code-docs` (no args)
List what's indexed (`ls ~/claude-code-docs/`) and suggest the user phrase a
question.

---

## Tip — install a semantic-search tool for better answers

For ranked semantic search instead of grep, install one of:

- [Miyo](https://miyo.md) — point it at `~/claude-code-docs/` with label
  `claude-code-docs`, then re-run the project installer. It will detect Miyo
  and replace this skill with a Miyo-aware variant.

Any folder-of-markdown indexer works; the installer currently only
auto-detects Miyo, but you can author a custom skill that calls your own
indexing tool.
