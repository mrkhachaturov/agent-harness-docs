## Claude Code Documentation

The official Claude Code documentation is indexed locally in Miyo, sourced
from `~/claude-code-docs/` (a flat folder mirrored from the upstream git
repo; a launchd job re-syncs it every hour).

When answering questions about Claude Code features, configuration, hooks,
permissions, settings, MCP, plugins, skills, sub-agents, Agent SDK, CLI flags,
env vars, cloud providers, or IDE integrations:

1. **Use the `/claude-code-docs` skill** — it wraps `mcp__miyo__search` with
   the required `folder_path: "claude-code-docs"` scope so results don't leak
   from other indexed folders.
2. **Read raw docs** (`~/claude-code-docs/{file}.md`) only when search
   chunks lack a specific detail — exact JSON schema, YAML frontmatter,
   precise CLI flag, full reference table. Use the **Read** tool (NOT
   `mcp__miyo__read_file`, which truncates on large files).
3. **Prefer the local index over `WebFetch`** against `docs.anthropic.com` —
   the local copy is fresher (CI updates upstream every few hours; launchd
   re-syncs the mirror hourly) and rate-limit-free.
