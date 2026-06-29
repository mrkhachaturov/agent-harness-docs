# Codebase indexing

Cursor indexes your codebase so Agent can find relevant code quickly. Code indexing runs automatically when you open a project.

## How does codebase indexing work?

When you open a project, Cursor scans and indexes your source files. This enables semantic search and gives Agent better context about your codebase. The index syncs periodically (roughly every five minutes) to pick up changes.

## How do I check codebase indexing status?

Look at the status bar at the bottom of Cursor. It shows the indexing progress when a scan is running.

## How do I reindex my project?

Open the command palette (Cmd + Shift + P on Mac, Ctrl + Shift + P on Windows/Linux) and search for "Reindex." Select the reindex command to rebuild the index from scratch.

## How can I speed up codebase indexing?

For large repositories, indexing can take time. To speed it up:

- Add large generated files and folders to `.cursorignore`
- Exclude `node_modules`, `dist`, and other build artifacts (these are ignored by default if in `.gitignore`)

## Related

- [Semantic search reference](https://cursor.com/docs/agent/tools/search.md)
- [Ignore files](https://cursor.com/help/customization/ignore-files.md)


---

## Sitemap

[Overview of all docs pages](/llms.txt)
