# Agent Harness Docs

[![Last Update](https://img.shields.io/github/last-commit/mrkhachaturov/agent-harness-docs/main.svg?label=docs%20updated)](https://github.com/mrkhachaturov/agent-harness-docs/commits/main)
[![Platform](https://img.shields.io/badge/platform-macOS%20%7C%20Linux%20%7C%20Windows-blue)](https://github.com/mrkhachaturov/agent-harness-docs)

A local Markdown mirror of the docs for four AI coding-agent harnesses, kept
fresh upstream and consumed through a small per-agent **skill** that searches
the docs with [Miyo](https://miyo.md).

| Docset | Source | Miyo folder label | ~pages |
|---|---|---|---|
| **Claude Code** | [code.claude.com](https://code.claude.com/docs/en/overview) | `claude-code` | ~150 |
| **OpenAI Codex** | [developers.openai.com/codex](https://developers.openai.com/codex) | `codex` | ~90 |
| **OpenCode** | [github.com/anomalyco/opencode](https://github.com/anomalyco/opencode) (MDX → MD) | `opencode` | ~35 |
| **Pi** | [github.com/earendil-works/pi](https://github.com/earendil-works/pi) | `pi` | ~27 |

> Forked from [ericbuess/claude-code-docs](https://github.com/ericbuess/claude-code-docs)
> and generalised to multiple harnesses.

## How it works

```
CI (every 3h) ──fetch──▶ docs/<docset>/*.md ──git pull──▶ your clone
                                                              │
                                          you index folders in Miyo
                                                              │
            /claude-code-docs  ──skill──▶ mcp__miyo__search(folder_path: "claude-code")
```

1. **Upstream**: a GitHub Actions job re-fetches all four sources every 3 hours
   and commits the result to `docs/<docset>/`.
2. **Local**: you `git pull` this repo whenever you want fresh docs, and point
   [Miyo](https://miyo.md) at the four `docs/<docset>/` folders, labelling them
   `claude-code`, `codex`, `opencode`, `pi`.
3. **Skills**: each agent gets a small `SKILL.md` that, when you invoke it,
   searches its docset via Miyo. The skills hold **no filesystem paths** — they
   address docs purely by Miyo folder label, so they are portable across
   macOS / Linux / Windows.

The skills are **manual-only** (`disable-model-invocation: true`): nothing loads
into an agent's context until you invoke it with `/<name>`, so they cost zero
idle context and never auto-trigger.

## Prerequisites

- **[Miyo](https://miyo.md)** — the semantic-search layer the skills call. Index
  each `docs/<docset>/` folder with the label from the table above.
- **Node** (for `npx`) — only to run the skill installer below.

## Install the skills

Skills are installed with the cross-agent [`skills`](https://skills.sh) CLI.
**Each docs skill goes to its own agent** — Claude Code doesn't need to know how
to configure Codex, so `claude-code-docs` installs only into Claude Code, and so
on:

```bash
# From GitHub (1:1 — each skill to its matching agent, global scope)
npx skills add mrkhachaturov/agent-harness-docs -g -a claude-code --skill claude-code-docs
npx skills add mrkhachaturov/agent-harness-docs -g -a codex        --skill codex-docs
npx skills add mrkhachaturov/agent-harness-docs -g -a opencode     --skill opencode-docs
npx skills add mrkhachaturov/agent-harness-docs -g -a pi           --skill pi-docs
```

- `-g` installs globally (available in every project); drop it to install into
  the current project only.
- `npx skills` symlinks by default (single source of truth — `npx skills update`
  refreshes). Pass `--copy` if your platform can't symlink.
- Install from a **local clone** (no GitHub push needed) by using `.` as the
  source: `npx skills add . -g -a claude-code --skill claude-code-docs`.

You only need the skill for an agent you actually use, and only for a docset
you've indexed in Miyo. Cross-install on purpose when it helps — e.g. give
Claude Code the `opencode-docs` skill while you're editing an `opencode.json`:

```bash
npx skills add mrkhachaturov/agent-harness-docs -g -a claude-code --skill opencode-docs
```

Manage later:

```bash
npx skills list -g                 # what's installed where
npx skills update -g               # pull latest SKILL.md
npx skills remove -g claude-code-docs
```

## Use

Invoke a skill with `/<name>` in its agent:

```text
/claude-code-docs how do hooks interact with permissions?
/claude-code-docs explain "sandbox environments"
/codex-docs        how do I configure AGENTS.md for nested directories?
/opencode-docs     how do I add a custom MCP server?
/pi-docs           how does session compaction work?
```

Each skill scopes its Miyo search to its own folder label, so results never
cross-contaminate between docsets.

## Refresh the docs

```bash
git pull            # CI updates docs/ upstream every few hours
```

**Miyo watches each indexed folder**, so it re-indexes the changed pages on its
own after a pull — no manual step. Per-file SHA-256 hashes in each
`docs/<docset>/docs_manifest.json` keep the re-embed diff small.

## Maintainer workflow

All tooling is pinned and orchestrated by [mise](https://mise.jdx.dev) — no
manual `pip`/`npm` installs. Entering the repo (`cd` in under `mise activate`)
installs the toolchain and project deps, and wires the local git hooks.

```bash
mise run fetch        # re-fetch all four docsets (or fetch:claude, fetch:codex, …)
mise run render       # regenerate skills/<docset>/SKILL.md from templates
mise run check        # quality gate: ruff lint + ruff format-check + render-check
mise run ci           # render + full check
```

- **Skills** are rendered from Jinja2 templates in
  [`skills/templates/`](skills/templates/) to `skills/<docset>/SKILL.md`. Edit a
  template, run `mise run render`, and commit both. CI (and `mise run check`)
  verify the rendered output is in sync.
- **OpenCode** docs need a Node MDX → Markdown step
  ([`scripts/mdx_to_md.mjs`](scripts/mdx_to_md.mjs)); `mise` provides Node and
  `mise run deps` runs `npm ci`.
- **Git hooks** ([`hk.pkl`](hk.pkl)) run safety checks plus `mise run check` on
  commit. They install locally on repo entry only (never in CI). Bypass once
  with `HK=0 git commit …`.

## License

Documentation content belongs to its respective authors — Anthropic (Claude
Code), OpenAI (Codex), the OpenCode project, and the Pi project. The fetchers,
renderer, templates, and skills in this repo are open source.
