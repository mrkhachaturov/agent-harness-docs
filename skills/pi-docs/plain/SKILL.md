---
name: pi-docs
description: Look up Pi coding-agent documentation in the local mirror at ~/pi-docs/. Use when answering questions about the Pi terminal coding harness, the `pi` CLI, extensions, skills, prompt templates, themes, pi packages, providers, models, settings, keybindings, sessions, compaction, the Pi SDK, RPC mode, JSON event stream, or TUI components.
---

# Pi Documentation (local mirror)

The official Pi docs are mirrored at `~/pi-docs/` — a flat folder
with ~27 `.md` files, auto-synced hourly from
`github.com/earendil-works/pi` (`packages/coding-agent/docs/*.md`).

## How to look up answers

No semantic-search tool is configured, so fall back to listing + grep:

1. **List or filter filenames** to find the relevant doc:
   ```
   ls ~/pi-docs/                                    # see all topics
   ls ~/pi-docs/ | grep -i skill                     # filenames mentioning skills
   ```
2. **Grep across the corpus** to find specific terms:
   ```
   grep -l -i "extension" ~/pi-docs/*.md             # files mentioning extensions
   grep -i "keybinding" ~/pi-docs/*.md               # exact term lookup
   ```
3. **Read the file** fully (or with offset/limit for large ones) once you know which doc has the answer.

## When to read the full file

Fetch the raw file when grep results do not contain the exact detail
needed — typical reasons:

- exact JSON schema for settings or extension manifests
- full keybindings table or theme key list
- precise CLI flag spelling or full slash-command catalog
- complete provider / model configuration reference

To read the raw file, use the standard read tooling with the absolute path:

```
Read("/Users/<you>/pi-docs/<filename>.md")
```

## File naming

Filenames match the upstream slugs at
`packages/coding-agent/docs/` directly:

- `index.md` (the overview / getting-started page)
- `quickstart.md`, `usage.md`, `providers.md`
- `extensions.md`, `skills.md`, `sdk.md`
- `sessions.md`, `session-format.md`

No subdirectories — the mirror is flat.

## Anti-patterns
- Do **not** use a web fetcher against `github.com/earendil-works/pi/` —
  the local mirror is fresher (CI updates upstream every few hours; launchd
  syncs the local mirror hourly) and rate-limit-free.

## Sub-commands the user may invoke

### `/pi-docs <question>`
Grep / scan the corpus for the question. Read the most likely files and
synthesize an answer with citations.
### `/pi-docs explain "<concept>"`
Run a broader grep, list all files that mention the concept, read the
top 2–3, and explain it covering: definition, configuration, related
features, gotchas.
### `/pi-docs path "<A>" "<B>"`
Grep for each concept, read the files that mention both, and explain how
they relate.
### `/pi-docs` (no args)
List what's indexed (`ls ~/pi-docs/`) and suggest the user phrase a
question.

---

## Tip — install a semantic-search tool for better answers

For ranked semantic search instead of grep, install one of:

- [Miyo](https://miyo.md) — point it at `~/pi-docs/` with label
  `pi-docs`, then re-run the project installer. It will detect Miyo
  and replace this skill with a Miyo-aware variant.

Any folder-of-markdown indexer works; the installer currently only
auto-detects Miyo, but you can author a custom skill that calls your own
indexing tool.
