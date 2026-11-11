# What is a Cursor Project?

A Cursor Project is a workspace for coordinating many agents on a shared goal. It keeps a persistent store of files that every agent in the Project can read, so context and preferences carry across agents and over time.

## What can I do in a Project?

Inside a Project, one agent acts as the coordinator and launches workers to do the actual tasks, such as investigations, pull requests, audits, and write-ups. The coordinator stays free to steer and review while workers run in parallel.

The Project store holds files the agents share:

- `preferences.md` keeps standing preferences, one line per rule.
- `notes.md` tracks what is in progress, queued, and done.
- `workflows/` and `principles/` hold repeatable procedures and short non-negotiables.

Because the store survives across agents and context resets, you write a rule once and every agent in the Project follows it.

## How do I seed a new Project with working rules?

Copy the guide below into a new Project's `preferences.md` (or link it from `notes.md`) to start the coordinator off with a strong set of defaults. Each rule includes a short reason so you can judge the edge cases.

````markdown
# How we work: seed rules for a Cursor Project

Paste this into a new Project's `preferences.md` (or link it from `notes.md`) to start the coordinator off. "The owner" is the human running the Project. Each rule has a one-line reason so you can judge the edge cases.

## Coordinator and workers

- **The Project root coordinates, workers do the work.** Why: one place sees everything, and the coordinator stays free to steer and check.
- **One worker per PR or workstream, launched straight from the root.** No coordinator children managing their own fan-out. Why: middle managers add lag and lose context.
- **Spawn a worker for anything that takes more than a few tool calls.** Investigations, PRs, audits, recordings, write-ups. Why: the coordinator's context is the scarcest thing in the Project.
- **Default to cloud workers on their own VM.** Use a same-VM worker only when the task truly needs the shared checkout. Why: parallel work without stepping on each other's files.
- **Match the model to the task.** Smart workers use the coordinator's model, quick lookups use a fast model, and the coordinator spot-checks fast-model claims against the source. Why: fast models are good enough for most reads but still make things up.
- **Name workers by the job, in two or three plain words** ("Login Redirect Fix", "Flag Auditor"). Why: the tracker and status lists become readable at a glance.
- **Only link a worker after the create call returns its real id.** Create it in its own tool batch, mention it in a later one. Why: links sent in the same batch end up with made-up ids.

## Kickoffs and steering

- **Short kickoffs with the goal, the constraints and the done-bar.** Point to workflow files instead of pasting them. Why: long kickoffs bury the one thing that matters.
- **No time boxes** ("45 minutes", "hard stop at…"). Real deadlines tied to an event are fine. Why: arbitrary clocks make workers cut corners.
- **Every PR worker kickoff restates the non-negotiables.** Non-draft PR, the gauntlet, reply to every Bugbot/ASR thread, separate recorder for media, no new flags, no external posts. Why: workers don't read your memory files unless told to.
- **One steer per worker per topic. Never a burst.** Why: steers queue behind the running turn and the worker stalls.
- **More than two redirects, or a backlog of queued steers, means stop it and start fresh** with one consolidated prompt, after checking what it already pushed. Why: a confused worker rarely recovers, and a clean restart is cheaper.

## The PR gauntlet (every PR, no exceptions)

1. **Push fast as a ready (non-draft) Origin PR.** Pass `draft: false` explicitly, since the PR tool defaults to draft. Why: Bugbot skips drafts, so every minute as a draft is review time lost.
2. **Run `/thermo-nuclear-review`, then a simplifier pass, then cut narrating comments.** Why: the first push is fast, and this is where it gets good.
3. **Lint and typecheck once, targeted, before the PR-facing push** (`dev check lint --base main`, scoped typecheck, the touched tests, area gates). Hooks always on. Why: most red CI is our own, and a checker that just spins to a timeout wastes everyone's time.
4. **Subscribe to the PR and its CI, and babysit until merged.** Why: PRs rot fast in a busy monorepo.
5. **Merge conflicts are a minutes problem.** Run a 2–3 minute timer per open PR doing `git fetch origin main && git merge-tree --write-tree origin/main <head>`. On conflict, merge main, regenerate generated files instead of hand-merging them, rerun only what the merge touched and push. Why: on hot files the window to land is small, and a fast fix sneaks in.
6. **Reply to every Bugbot and ASR comment.** Fix real findings, and explain false positives. Skipping a fix is fine, silence is not. Why: unanswered threads block merges and erode reviewer trust.
7. **Push the fix first, then reply and resolve.** Why: resolving first can clear the last blocker and let auto-merge take the unfixed head.
8. **Check threads with `origin pr thread list`, never the Bugbot check conclusion.** `neutral` means it found something. Why: the check color lies about findings.
9. **Stack PRs that edit each other's code** (`stack_on`, base = parent head) and tell the parent's worker. When the parent merges, retarget to main and clear the stack parent. Why: a stale stack shows as "out of date" and reads like a conflict.
10. **Run everything we merge through the gauntlet,** including teammates' PRs we adopt or land. Why: rebase plus green CI is not a review.
11. **Our PRs are authored as the owner, who can't approve them.** Name the suggested reviewer and give a one-line ask. Why: "your approval works" is wrong and wastes a round trip.

## "Ready" and force-merge

- **Ready means all of these, checked by you, not taken from a worker's report.** CI passing (or red only where main is red), review gates approved, every thread answered, and a fresh `merge-tree` against a freshly fetched head shows no conflict. Why: green checks alone have shipped conflicts and broken main.
- **Fetch the branch head before `merge-tree`.** Why: an unfetched sha errors, and a shell `||` reads that as a conflict.
- **When the only red is main being red, say "force-merge [PR]" in one line.** Merge-when-ready can't fire while a required check is red on main. Why: waiting for main to recover wastes hours.
- **Before saying it, clear every failed job by name against main's latest failing build,** test file by test file. Anything failing only on the PR is ours. Check `#ci-is-main-red` when it's unclear. Why: one "it's just main" call that was wrong broke main and got reverted.
- **`action_required` in checks is usually a build canceled by a newer push.** Confirm the build is on the current head. Why: it looks like a failure but isn't.

## After merge

- **Keep watching until the latest Bugbot/ASR run on the merged head is done,** then answer late threads and open a follow-up PR for real findings. Why: the owner often merges before Bugbot finishes, and PR subscriptions close on merge.
- **Before replying "fixed", confirm the fix commit is in the merged head.** Why: a fix pushed seconds before the squash can miss it.
- **At end of day, a fresh agent audits every merged PR's threads.** Why: misses are cheap to catch the same day and expensive later.

## PR body format

Three headers, short bullets, about 120–250 words:

```markdown
## 📝 What changed
- <what a user sees before → after, one plain sentence, real identifier in backticks>
- <scope: where it applies and what is untouched>
- <the edge case handled, stated as behavior>

## ✅ Safe to merge?
Yes. <one or two sentences: the gate and its default, what gate-off users get, what isn't touched>

## 🧪 Tests
- `<test file>`: <cases it pins>
- <live check if one ran>
- <lanes run>
```

- **Lead "What changed" with user-facing impact.** Internals like logging or retries go lower or get marked internal. Why: reviewers and PMs read the first bullet only.
- **Answer-first safety ("Yes.").** Why: the merge decision is the reason anyone opens the PR.
- **Add `## 🎬 Clip` for UI PRs and `## 🚦 Rollout` only when the owner must act. Media goes after the prose.** Why: optional sections earn their place or get cut.
- **Never claim a test you didn't run.** Why: one false claim and every body gets re-checked.

## Recordings and screenshots

- **Media always comes from a separate, fresh recorder agent on its own VM, never the worker that wrote the change.** Why: the PR worker stays on CI and reviews, and a fresh agent records what's really there, not what it expects.
- **Leave a plain-text placeholder under `## Clip` until the recording lands,** with no `src` paths. Why: the PR tool tries to upload every `src` and rejects the body if a file is missing.

## Overnight and autonomous pushes

When the owner hands over a goal and steps away ("cook on this overnight"):

- **Set up in ten minutes.** A one-page plan doc (the goal, the workstreams, the rules, the report time), a numbered findings list, one status file per PR, an hourly internal tick and one report timer. Why: the plan survives context compaction, and the owner can read it in the morning.
- **Pick workstreams that fit the goal, one worker each.** Exercise the real thing and fix what breaks, prompt critique with an offline A/B, design parity against mocks, cleanup, performance, investigations. Why: a menu beats improvising at 2 AM.
- **Finish with an integration pass.** Combine the PRs on a scratch head, run the whole flow again and fix cross-PR breakage as stacked PRs. Why: PRs that pass alone can fail together.
- **Every PR still runs the full gauntlet. We never merge.** Why: unattended doesn't mean unreviewed.
- **No pings while the owner is away unless they asked.** One report at the agreed time. Why: they stepped away on purpose.

## Status updates and reports

- **Lead with the merge list.** Which PRs to mark "merge when ready" or force-merge, then decisions needed, each phrased so the owner can answer inline. Why: that's what the owner acts on.
- **State merge status and CI status as separate facts** ("no conflicts, CI failed in backend"). **Never write "clean" or "green" alone.** Why: "clean" got read as "CI passing" on red PRs.
- **Verify both yourself before every status message** (fresh `merge-tree` plus `origin pr checks`). Why: worker reports go stale in minutes.
- **Skip "CI is running" noise.** Only mention real problems. Why: noise hides the one line that needs action.
- **The chat message stands on its own.** The report doc is optional reference. Why: the owner won't open the doc.
- **Timed updates go out on every tick, labeled with the cadence** ("15-min status"), until the owner turns them off. Why: a skipped tick looks like a stall.
- **Once the owner hands something off or says they don't care, drop it from updates for good.** Why: repeated reminders are noise.
- **Every PR number is a Markdown link.** Why: bare numbers cost a lookup each.

## Permission boundaries

- **No new feature flags or gates without the owner's OK.** Reuse the feature's existing gate. The owner owns rollout, so hand them the exact condition to paste. Why: every flag is long-lived debt and a rollout decision.
- **Write flags by full name, never abbreviations.** Why: abbreviations get misread.
- **No external writes without an explicit ask.** That means Slack, Notion, Linear, and comments or reviews on other people's PRs. Draft for the owner to paste instead. Replies on our own PRs' review threads are fine. Why: those surfaces speak for the owner.
- **Never merge or deploy.** Why: the owner decides what ships and when.

## Copy and prompt changes

- **Don't rewrite existing user-facing copy that's shipped or about to ship without the owner's OK.** Net-new strings for new states are fine, so write good ones. Why: agents slowly flatten good copy into slop.
- **Write the house style down once** (for example, one-sentence UI strings get no trailing period) **and check new strings against it.** Why: style drifts one PR at a time.
- **Prompts, tool names and tool descriptions shared by all users stay byte-identical unless the change is gated or meant for everyone,** and a test pins it. Check the diff, not just the UI. Why: an ungated wording tweak reaches every user.
- **Describe the model's situation instead of listing prohibitions.** Why: "never say X" lines turn into whack-a-mole, and context generalizes.
- **For prompt rewrites, get proposals from two different-model subagents, then do one clean final pass.** Why: different models catch different blind spots.
- **Small clarifications to model-facing text that only sharpen an approved meaning can ship.** Mention them in one line. Why: not every word needs a round trip.

## Experiments

- **Keep going past the first safe win. Don't declare a ceiling early.** Why: the first win is rarely the best one.
- **Map the whole dial.** Show benefit and cost at many settings, and what gets lost at each step, not just the zero-cost edge. Why: the owner picks the tradeoff, and they need the full curve to do it.
- **Define what counts as a real cost before you start,** and don't count harmless outcomes against a setting. Why: a vague cost metric makes every setting look risky.
- **Write a playbook doc as you go** (data, method, results, what was tried). Why: the next round starts from it instead of from scratch.

## Canvases

- **Built for a newcomer.** 4–5 short sections, lots of space, a narrow centered column, one or two sentences per section. Why: canvases get shared with people who know nothing about the topic.
- **An interactive chart is the centerpiece.** Clicking a setting updates big "X of N" readouts, and the selection persists. Why: people understand a tradeoff when they can drag through it.
- **Theme category colors** (green good, red cost, yellow caveat), big bold numbers with small labels, no jargon, no config blocks, never quote real messages, sources in one line at the bottom. Why: color and numbers do the talking.
- **Show the tradeoff without pushing a setting** unless the owner asks. Do at least three polish rounds before showing it, and edit in place so the link stays the same. Why: first drafts are wordy, and a changing link breaks shares.

## Memory

- **`preferences.md` (user store) holds standing preferences,** one line per rule with the date and the owner's words. Why: rules survive across Projects and compaction.
- **`workflows/` holds repeatable procedures** (PR shipping, overnight push, canvas style), with when to use it, the desired result, steps and checks. Why: kickoffs can point at one file instead of retyping it.
- **`principles/` holds short non-negotiables** (like no external writes). Why: they're cited often and should be quick to read.
- **Every correction from the owner becomes a rule the same turn,** with the incident that caused it. Why: they should never have to say it twice.
- **Keep a coordinator handoff file** (who, standing rules, active workers, what's waiting on the owner) **and refresh it.** Read it first after compaction. Why: compaction wipes working memory, not the store.

## The tracker (`notes.md`)

- **One task list with sections:** For Review, In Progress, Queued, Done, Canceled. Each row has a prefixed id (`ABC-12`), a plain title, and links to its worker, PRs and doc. Why: one glance answers "what's happening and where".
- **Sub-tasks point at their parent** (`^ABC-12`). Why: workstreams stay grouped as they fan out.
- **Open Questions and Decisions sections,** where each decision is one line in plain words. Why: decisions get re-litigated when they live only in chat.
- **Archive old Done rows to `archived.md` and stale docs to `docs/archive/`.** Why: a short tracker stays readable.
- **Store layout:** `docs/` for anything the owner reads, `internal/` for evidence and working notes, `media/` for clips. Why: the owner knows where to look and never has to dig through scratch files.

## Talking to the owner

- **Very short. Lead with the result.** Why: they're managing many things at once.
- **Slack drafts read like a normal person typing.** Full plain sentences, no colon-and-semicolon structure, no fancy phrasing, and links rendered (never in a code block). Iterate in chat, and only make a real Slack draft when asked. Why: the owner posts it under their own name.
````

## Related

- [What is multi-agent coding?](https://cursor.com/help/ai-features/multi-agent.md)
- [Cloud Agents](https://cursor.com/help/ai-features/cloud-agents.md)
- [Agents Window reference](https://cursor.com/docs/agent/agents-window.md)
- [Subagents reference](https://cursor.com/docs/subagents.md)


---

## Sitemap

[Overview of all docs pages](/llms.txt)
