# Cloud Agent Builds

Builds prepare your Cloud Agent environment in the background. Each agent starts from a pre-built machine with your repositories, tools, and dependencies ready.

## Opt an existing environment into Builds

New environments use Builds by default. To enable Builds for an existing environment:

1. Open **Environments** in the [Cloud Agents dashboard](https://cursor.com/dashboard/cloud-agents#environments).
2. Select an environment and open its **Builds** tab.
3. Choose one of these setup paths:
   - Select **Run set up check first** to let an agent inspect your environment, test a Build, and propose any needed changes.
   - Select **Enable Builds** to enable Builds and create one with your current configuration.
4. Confirm the first Build succeeds before using it for agent runs.

The setup agent checks which commands should run during a Build and which need to run when an agent starts. For dashboard-managed environments, it proposes an updated configuration for you to review and save. For environments defined in `.cursor/environment.json`, it can open a pull request with the changes.

You can select **Run test Build** from the Builds tab to test your configuration without enabling Builds for all agent runs. The setup agent doesn't enable Builds for you. Select **Enable Builds** when you're ready.

## How Builds work

A Build is a bootable snapshot of a prepared Cloud Agent environment. Cursor creates Builds ahead of agent runs and keeps the latest successful one ready to start.

Each Build follows this lifecycle:

1. **Trigger**: A Build starts on a schedule, after you save an environment version, from a manual request, or at an agent's request.
2. **Prepare**: Cursor starts from your base image, clones every repository in the environment at its default branch, and runs the `install` command to completion.
3. **Snapshot**: Cursor saves the machine's disk state with the environment version and exact commit SHA for each repository.
4. **Activate**: A successful Build becomes active unless the environment is pinned to another Build.
5. **Start agents**: New agents, automations, and code reviews start from the active Build.

Cursor keeps pre-warmed copies of active Builds ready. This removes repository cloning and dependency installation from the agent startup path.

If a new Build fails, agents continue to use the last successful Build. A broken dependency update, install command, or Dockerfile doesn't replace the active environment.

## What runs during a Build and an agent start

Use each environment command for a distinct phase:

| Command     | When it runs                   | Use it for                                                                             |
| :---------- | :----------------------------- | :------------------------------------------------------------------------------------- |
| `install`   | During each Build              | Installing dependencies, generating code, compiling artifacts, and warming disk caches |
| `start`     | At the start of each agent run | Starting Docker, databases, tunnels, and other services                                |
| `terminals` | At the start of each agent run | Starting app processes in `tmux` terminals shared with the agent                       |

Make `install` complete and idempotent. It can run repeatedly and may run on top of previously prepared disk state. Commands such as `npm install`, `pnpm install`, and `pip install` already support this pattern.

Builds preserve disk state only. Running processes, shell exports, and
in-memory caches stop when Cursor snapshots the machine. Put services and
other session-specific work in `start` or `terminals`.

Your existing environment inputs still apply. Builds use saved snapshots, `.cursor/environment.json`, Dockerfiles, install and startup commands, secrets, and network settings.

## How Builds handle Git state

A Build records the commit checked out for each repository when it runs.

- **Default branch runs** start from the commit recorded in the active Build. Scheduled Builds run hourly by default, and you can change the frequency. Fetch or fast-forward from `start` if every run needs the latest default branch commit.
- **Feature branch runs** start from the active Build's prepared disk, then Cursor checks out the requested branch. The source code matches the branch you selected while reusing dependencies from the Build.
- **Multi-repo environments** record one commit per repository and prepare the complete workspace together.

If a feature branch changes dependencies, the agent receives your environment context and install command so it can refresh the environment before testing.

## How secrets work with Builds

Builds can access team and environment secrets. Use these for private package registries, artifact stores, and other credentials required by `install`.

User secrets are added only when an agent starts. They aren't available during Builds and don't become part of a shared snapshot.

Saving environment configuration or changing its secrets triggers a new Build.

## Manage Builds

Open an environment's **Builds** tab to:

- See every Build's status, trigger, duration, environment version, and repository commits
- Open a Build to inspect its events and logs
- Run a Build on demand
- Choose the active Build
- Pin an environment to a Build so newer successful Builds don't activate automatically
- Invalidate a Build so it can't become active
- Change the scheduled Build frequency
- Start an agent from a specific Build

Every agent run records the Build it started from. Use this provenance to compare environment behavior with the exact configuration and repository commits in the Build.

## Debug a Build

Open a failed Build to inspect its events and logs. Agents continue to start from the active successful Build while you diagnose the failure.

For an exact reproduction, start an agent from the failed Build. The agent opens the machine in its failed state, where it can inspect logs, update the environment, run a test Build, and verify the result.

You can also ask a Cloud Agent to inspect and manage Builds through the built-in [Cursor Cloud MCP](https://cursor.com/docs/cloud-agent/capabilities.md#cursor-cloud-mcp). For example:

```text
Inspect the latest failed Build for this environment. Fix the environment
configuration, run a test Build, and verify it before proposing the final
install and start commands.
```

## Build behavior reference

### Which Build does an agent use?

By default, an agent uses the latest successful active Build for its environment. A pinned environment continues to use the pinned Build until you remove the pin or select another one.

You can also start an agent from a specific Build when testing or debugging.

### What happens before the first successful Build?

Agents use the standard environment startup flow until the first Build completes successfully. A failed Build doesn't interrupt existing agent workflows.

### How fresh is the source code?

Feature branch runs check out the requested branch after the Build starts. Default branch runs begin at the commit recorded by the active Build, which is usually no more than one scheduled Build interval old.

### Do Builds replace snapshots or Dockerfiles?

No. A saved snapshot or Dockerfile defines the base machine used to create a Build. Cursor then clones the repositories, runs `install`, and creates a fresh bootable snapshot.

### Do Builds expire?

Active healthy Builds don't expire. Cursor may clean up older inactive Builds.

### Do Builds support multiple repositories?

Yes. One Build prepares all repositories in the environment and records the commit used for each one.

### Do Builds cost extra?

No. Builds are included with Cloud Agents.

## Related

- [Cloud Environment Setup](https://cursor.com/docs/cloud-agent/setup.md)
- [Cloud Agent capabilities](https://cursor.com/docs/cloud-agent/capabilities.md)
- [Cloud Agents settings](https://cursor.com/docs/cloud-agent/settings.md)


---

## Sitemap

[Overview of all docs pages](/llms.txt)
