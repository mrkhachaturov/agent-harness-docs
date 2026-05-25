---
name: codex-docs
description: Look up OpenAI Codex documentation in the local mirror at ~/codex-docs/. Use when answering questions about the Codex CLI, Codex app, IDE extension, cloud threads, AGENTS.md, config.toml, MCP servers in Codex, skills, plugins, hooks, sandboxing, approvals, slash commands, the Codex SDK, app-server, or the Codex GitHub Action.
---

# Codex Documentation (local mirror)

The official Codex docs are mirrored at `~/codex-docs/` — a flat folder
with ~80 `.md` files, auto-synced hourly from `developers.openai.com/codex`.

## How to look up answers

No semantic-search tool is configured, so fall back to listing + grep:

1. **List or filter filenames** to find the relevant doc:
   ```
   ls ~/codex-docs/                                 # see all topics
   ls ~/codex-docs/ | grep -i mcp                    # filenames mentioning MCP
   ```
2. **Grep across the corpus** to find specific terms:
   ```
   grep -l -i "AGENTS.md" ~/codex-docs/*.md          # files mentioning AGENTS.md
   grep -i "sandbox_mode" ~/codex-docs/*.md          # exact term lookup
   ```
3. **Read the file** fully (or with offset/limit for large ones) once you know which doc has the answer.

## When to read the full file

Fetch the raw file when grep results do not contain the exact detail
needed — typical reasons:

- exact TOML schema or full `config.toml` key list
- precise CLI flag spelling or option list
- the full table of an env-var / settings / hook event reference
- the complete catalog of slash commands

To read the raw file, use the standard read tooling with the absolute path:

```
Read("/Users/<you>/codex-docs/<filename>.md")
```

## File naming

The mirror flattens the URL path with `__` as the separator:

- `developers.openai.com/codex/quickstart` → `quickstart.md`
- `developers.openai.com/codex/app/automations` → `app__automations.md`
- `developers.openai.com/codex/concepts/sandboxing` → `concepts__sandboxing.md`

## Anti-patterns
- Do **not** use a web fetcher against `developers.openai.com/codex/` — the
  local mirror is fresher (CI updates upstream every few hours; launchd
  syncs the local mirror hourly) and avoids Vercel's bot-protection layer.

## Sub-commands the user may invoke

### `/codex-docs <question>`
Grep / scan the corpus for the question. Read the most likely files and
synthesize an answer with citations.
### `/codex-docs explain "<concept>"`
Run a broader grep, list all files that mention the concept, read the
top 2–3, and explain it covering: definition, configuration, related
features, gotchas.
### `/codex-docs path "<A>" "<B>"`
Grep for each concept, read the files that mention both, and explain how
they relate.
### `/codex-docs` (no args)
List what's indexed (`ls ~/codex-docs/`) and suggest the user phrase a
question.

---

## Tip — install a semantic-search tool for better answers

For ranked semantic search instead of grep, install one of:

- [Miyo](https://miyo.md) — point it at `~/codex-docs/` with label
  `codex-docs`, then re-run the project installer. It will detect Miyo and
  replace this skill with a Miyo-aware variant.

Any folder-of-markdown indexer works; the installer currently only
auto-detects Miyo, but you can author a custom skill that calls your own
indexing tool.
