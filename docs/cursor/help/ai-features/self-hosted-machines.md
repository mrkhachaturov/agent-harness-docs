# Self-Hosted Machines

Self-Hosted Machines moves Cloud Agent tool execution to hardware you manage. Cursor-managed Cloud Agents stay the default. The agent loop stays in Cursor's cloud. Your machine runs the tools.

## How do I connect a Self-Hosted Machines worker in a few minutes?

Install the [Cursor CLI](https://cursor.com/docs/cli/overview.md), then pick one path.

**My Machines** (one engineer, one box):

```bash
curl https://cursor.com/install -fsS | bash
agent login
cd /path/to/repo
agent worker start --name "my-devbox"
```

Use a [personal API key](https://cursor.com/dashboard/api) instead of browser login when the machine has no browser:

```bash
agent worker --api-key "$CURSOR_API_KEY" --name "my-devbox" start
```

**Team Pools** (shared team fleet):

```bash
export CURSOR_API_KEY="<service-account-api-key>"
cd /path/to/repo
agent worker --pool start
```

Team pool workers need a [service account API key](https://cursor.com/docs/account/enterprise/service-accounts.md). Personal API keys register a My Machines worker, not a team pool worker.

Team admins must enable self-hosted workers in the [Cloud Agents dashboard](https://cursor.com/dashboard/cloud-agents#self-hosted-agents) before members can connect team pool workers.

Keep the process running. The worker connects outbound over HTTPS. No inbound ports or VPN are required.

## Which Self-Hosted Machines path should I use?

| You care about                 | Likely path                                                                                                                                                                                  |
| ------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Perimeter or compliance only   | Start with managed Cloud Agents and [private connectivity](https://cursor.com/docs/cloud-agent/private-connectivity.md). Use a team pool only when you also need execution on your hardware. |
| One engineer, one box          | [My Machines](https://cursor.com/help/ai-features/self-hosted-machines.md#what-is-the-difference-between-a-team-pool-and-my-machines)                                                        |
| Org fleet, Kubernetes, or GPUs | [Team Pools](https://cursor.com/help/ai-features/self-hosted-machines.md#what-is-the-difference-between-a-team-pool-and-my-machines)                                                         |
| A partner VM or sandbox        | [Integrations](https://cursor.com/docs/cloud-agent/self-hosted/integrations.md)                                                                                                              |
| You do not want to run infra   | Managed Cloud Agents                                                                                                                                                                         |
| "Is Cursor on-prem now?"       | No. See [Is Cursor on-prem now?](https://cursor.com/help/ai-features/self-hosted-machines.md#is-cursor-on-prem-now)                                                                          |

## What are Self-Hosted Machines for Cloud Agents?

Cursor keeps the agent loop: inference and planning. Your source code, secrets, and tool execution stay on your machine.

You can run workers on a VM, Kubernetes node, Mac, GPU box, or a [partner sandbox](https://cursor.com/docs/cloud-agent/self-hosted/integrations.md). Common reasons to use Self-Hosted Machines:

- Custom hardware, such as GPUs or Macs for iOS work
- Secrets and build artifacts that must stay in your infrastructure
- Private Git or package registries your machine can already reach
- Sandboxes where you manage cloning and git state yourself

If your only concern is reaching private source control from Cursor's cloud, try managed Cloud Agents with [private connectivity](https://cursor.com/docs/cloud-agent/private-connectivity.md) before you operate your own workers.

## Is Cursor on-prem now?

No. Cursor is not an on-prem product. The agent loop stays in Cursor's cloud. You register a machine you operate, and Cursor sends tool calls to it over an outbound HTTPS connection.

Your checkout, build cache, and machine-local credentials stay on your hardware. See [What data stays on my machine vs. in Cursor's cloud?](https://cursor.com/help/ai-features/self-hosted-machines.md#what-data-stays-on-my-machine-vs-in-cursors-cloud) for the full split.

## How does Self-Hosted Machines connectivity differ from managed Cloud Agents?

Both options keep the agent loop in Cursor's cloud. They differ in where tool execution runs and how private repos and internal tools are reached.

|                                       | Managed Cloud Agents                                                                                                                      | Self-Hosted Machines                                                               |
| ------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| **Where tools run**                   | Cursor-managed VMs in Cursor's cloud                                                                                                      | A machine you operate (VM, Kubernetes node, laptop)                                |
| **Network direction**                 | Cursor connects into your environment when you set up [private connectivity](https://cursor.com/docs/cloud-agent/private-connectivity.md) | Your worker connects **outbound** to Cursor over HTTPS                             |
| **Private Git or registries**         | Use PrivateLink or Cloudflare Tunnel so Cursor's cloud can reach your SCM over a private path                                             | The worker uses **local** network access, PATs, or SSH keys already on the machine |
| **Inbound firewall rules for Cursor** | Often required for private connectivity endpoints or tunnels                                                                              | **Not required**. Cursor never connects into your network                          |
| **HTTP MCP servers**                  | Cursor backend reaches hosted MCP URLs                                                                                                    | Cursor backend still reaches hosted MCP URLs                                       |
| **Command (`stdio`) MCP**             | Runs in the Cursor VM unless configured otherwise                                                                                         | Runs on your worker and can reach private endpoints                                |

Choose managed Cloud Agents with [private connectivity](https://cursor.com/docs/cloud-agent/private-connectivity.md) when you want Cursor to operate the execution environment but still reach private source control from Cursor's cloud.

Choose Self-Hosted Machines when execution must stay on hardware you control and that hardware can already reach your repos and internal services. You do not open inbound HTTPS for Cursor to reach your tools. The worker reaches them locally and reports results back over the outbound session.

See [Do Self-Hosted Machines require inbound network access or a VPN?](https://cursor.com/help/ai-features/self-hosted-machines.md#do-self-hosted-machines-require-inbound-network-access-or-a-vpn) for outbound hosts and [Cloud Agents](https://cursor.com/help/ai-features/cloud-agents.md) for managed setup.

## What is the difference between a team pool and My Machines?

|                    | Team Pools                                                 | My Machines                                |
| ------------------ | ---------------------------------------------------------- | ------------------------------------------ |
| **Who uses it**    | Shared team fleet                                          | One person's machine                       |
| **Authentication** | Service account API key                                    | `agent login` or personal API key          |
| **CLI**            | `agent worker --pool start`                                | `agent worker start --name "…"`            |
| **Routing**        | Any team member's request can route to an available worker | Sessions route to machines on your account |
| **Typical use**    | Company-wide capacity, Kubernetes, GPU fleets              | Personal devbox, Mac, or remote VM         |

A team pool is a named routing target. Chats wait in the team pool until a worker claims them. One agent claims each team pool worker at a time.

My Machines (also called Remote Control) connects one machine you own. Multiple agents can run on the same machine when it has enough resources.

For Kubernetes fleets, use the Helm chart and `WorkerDeployment` operator. See the [Kubernetes deployment guide](https://cursor.com/docs/cloud-agent/self-hosted/kubernetes.md).

Team Pools require an Enterprise plan and a [service account API key](https://cursor.com/docs/account/enterprise/service-accounts.md). [My Machines](https://cursor.com/docs/cloud-agent/self-hosted/my-machines.md) uses a personal credential.

## How do admins enable or require Self-Hosted Machines?

Team admins open the [Cloud Agents dashboard](https://cursor.com/dashboard/cloud-agents#self-hosted-agents) and go to **Self-Hosted** settings.

- **Allow Self-Hosted Machines**: members can opt in to runs on machines they connect. Without opt-in, Cloud Agents use Cursor's managed infrastructure.
- **Require Self-Hosted Machines**: every Cloud Agent session must use a self-hosted machine.

The dashboard also shows team pool details and machines registered under **My Machines**.

## Can I run Self-Hosted Machines on a third-party VM or sandbox?

Yes. Team pool workers can run on a partner platform, or from a reference template you clone. Cursor still runs the agent loop. The worker on that VM or sandbox runs tools and connects outbound over HTTPS.

See [Integrations](https://cursor.com/docs/cloud-agent/self-hosted/integrations.md) for the partner guides and templates.

Partner guides cover AWS Lambda, Cloudflare, Namespace, Modal, Daytona, E2B, and Vercel. Reference templates cover AWS Lambda MicroVMs, Cloudflare Containers, and Kubernetes.

You can also install the Cursor CLI on a VM you already run and start a worker yourself with `agent worker start` or `agent worker --pool start`.

## Do Self-Hosted Machines require inbound network access or a VPN?

No. The worker initiates a single outbound HTTPS connection from your machine to Cursor's cloud. Cursor sends agent requests down that connection. Your machine never needs to be reachable from the internet.

You do not need inbound ports, firewall changes, or VPN tunnels. If your network uses an HTTPS proxy, set `HTTPS_PROXY` or `https_proxy` in the worker environment.

Workers need outbound access to `api2.cursor.sh`, `api2direct.cursor.sh`, and `cloud-agent-artifacts.s3.us-east-1.amazonaws.com` for artifact uploads. See [What leaves your network](https://cursor.com/docs/cloud-agent/self-hosted.md#what-leaves-your-network) for the full data flow.

## What data stays on my machine vs. in Cursor's cloud?

Your source code, build artifacts, secrets, and tool execution stay on your machine. That includes file edits, terminal commands, and network calls the agent makes locally.

Cursor's cloud handles the agent loop: inference requests and planning. Results from tool calls flow back to Cursor for the next inference round, but your raw code and secrets are not stored in Cursor-managed infrastructure.

[Privacy Mode](/data-use) applies the same way it applies to managed Cloud Agents. When enabled, code sent from the worker is not used for training by Cursor or model providers.

## Can I use a team pool for any repository without specifying one?

Yes. Any-repo team pools decouple source control from the team pool. One team pool can serve many repositories.

```bash
agent worker --pool sandbox --worker-dir "$HOME/cursor-sandboxes/default" start
```

Pass `--clone-git-repos` so the worker clones repos on claim. In the Cursor composer environment picker, select the team pool under **Any repo**.

Repo-backed team pools still work when workers serve specific checkouts. Pass `--worker-dir` once per repo root.

## How do I connect private or self-hosted GitLab?

For private or air-gapped self-hosted GitLab, use an [any-repo team pool](https://cursor.com/help/ai-features/self-hosted-machines.md#can-i-use-a-team-pool-for-any-repository-without-specifying-one) so the SCM lifecycle stays on your workers.

1. Create a team pool without binding it to one repository.
2. Start workers from a workspace directory on a machine that can reach your GitLab instance.
3. Authenticate git with a local personal access token or SSH key on the worker. You do not need Cursor's GitLab OAuth for the worker checkout.

The agent accesses private repos through the network access your machine already has. This pattern also helps when developers work across many repositories.

See the [GitLab integration docs](https://cursor.com/docs/integrations/gitlab.md) for OAuth-based Cloud Agent setup on managed infrastructure.

## Can agents use the screen or browser on a Self-Hosted Machines worker?

Yes, on macOS and Linux workers. Install desktop packages on Linux first, then start with `--computer-use`:

```bash
agent worker --computer-use start
```

On macOS, the first start installs the Cursor Computer Use helper. Grant it Accessibility and Screen Recording. Desktop sharing with `--share-desktop` is Linux-only. For browser use, install Chrome or Chromium on the runner.

See [Computer use and desktop sharing](https://cursor.com/docs/cloud-agent/self-hosted/computer-use.md) for dependencies and setup.

## Do hooks and MCP work on Self-Hosted Machines?

Yes, with some differences from managed Cloud Agents.

**Hooks**: Workers run project hooks from `.cursor/hooks.json`. Enterprise plans also get team hooks and enterprise-managed hooks on self-hosted workers. `sessionStart` and `sessionEnd` run when a session claims a worker and when that claim is released. See the [hooks support matrix](https://cursor.com/docs/hooks.md#cloud-agent-support) and [Hooks on Team Pools](https://cursor.com/docs/cloud-agent/self-hosted/pool.md#hooks).

**MCP**: Command (`stdio`) MCP servers run on your worker and can reach private networks. HTTP and SSE servers still run from Cursor's backend. Some MCP gaps remain on self-hosted workers; check the [changelog](https://cursor.com/docs/cli/changelog.md) for the latest status.

## How do I troubleshoot a Self-Hosted Machines setup?

Start with these basics:

1. **Check the dashboard.** Open the [Cloud Agents dashboard](https://cursor.com/dashboard/cloud-agents#self-hosted-agents) and confirm workers show as connected, idle, or in use under **My Machines** or team pool details.
2. **Run diagnostics.** Run `agent worker debug` for worker preflight checks (add `--json` for machine-readable output). The report covers auth, connectivity, routing, and backend visibility.
3. **Worker missing from the UI.** If the worker process is running locally but does not appear in Cursor, the cause is usually outbound connectivity. Confirm the machine can reach `api2.cursor.sh` and `api2direct.cursor.sh` over HTTPS. See [Do Self-Hosted Machines require inbound network access or a VPN?](https://cursor.com/help/ai-features/self-hosted-machines.md#do-self-hosted-machines-require-inbound-network-access-or-a-vpn).
4. **Team pool controller issues.** The built-in [worker controller](https://cursor.com/docs/cloud-agent/self-hosted/pool.md#worker-controller) is new. Treat controller and autoscaling setups as early deployments and document fixes as patterns emerge on your team.

Worker preflight report:

```bash
agent worker debug
```

The report covers authentication, connectivity, routing, repository labels, and whether Cursor can see your worker.

Common fixes:

- Confirm the worker process is still running
- Confirm the Cursor app and CLI use the same account
- Check that the worker directory has the expected Git remote for repo-backed workers
- Check outbound HTTPS access to the hosts listed in [What leaves your network](https://cursor.com/docs/cloud-agent/self-hosted.md#what-leaves-your-network)

For connection issues before the worker starts, run `agent worker start --debug`. Include `agent worker debug` output when you [contact support](https://cursor.com/help.md) about persistent setup problems.

### How do I make sure SCM permissions are honored?

Self-hosted runs use two layers: Cursor routing (which worker serves a request) and git credentials on the worker (what that worker can clone, fetch, or push).

**Cursor routing**

- **My Machines**: Cursor only routes a repository request to a worker when one of its registered `--worker-dir` roots matches that repo. Start the worker from the correct checkout or add another `--worker-dir`.
- **Repo-backed team pools**: Requests match both the team pool name and a `repo=<owner/repo>` label. A request for `pool=gpu` and `repo=acme/payments` routes only to a worker serving that repo.
- **GitHub triggers**: On public repos, only users with `OWNER` or `COLLABORATOR` access can route a run to a self-hosted team pool. Other commenters stay on managed infrastructure unless your team requires self-hosted for all runs.
- **Org controls**: [Protected Git Scopes](https://cursor.com/docs/enterprise/model-and-integration-management.md#protected-git-scopes) and the [repository blocklist](https://cursor.com/docs/enterprise/model-and-integration-management.md#git-repository-blocklist) still apply. Connect each user's Git account under [Integrations](https://cursor.com/dashboard/integrations) so Cursor can verify repository access before a run starts.

**Git access on the worker**

- **Existing checkouts** (My Machines or repo-backed team pools): The agent uses git credentials already on the machine, such as SSH keys or a personal access token in your credential helper. Grant each worker only the repo access it needs.
- **Any-repo team pools with `--clone-git-repos`**: The worker clones on claim using a short-lived GitHub token minted for the user who started the run. A team admin must enable GitHub token minting for team pool workers, and the requesting user must have access to that repository in GitHub.
- **Private or self-hosted GitLab**: Authenticate git on the worker with a local PAT or SSH key. See [How do I connect private or self-hosted GitLab?](https://cursor.com/help/ai-features/self-hosted-machines.md#how-do-i-connect-private-or-self-hosted-gitlab).

**When git fails but the worker is connected**

1. Run `agent worker debug` and confirm repository labels match the repo in the request.
2. On the worker, run `git fetch` or `git ls-remote` with the same credentials the agent will use.
3. Confirm the Cursor user who started the run can access the repository in your Git provider and in Cursor Integrations.
4. For team pool clone-on-claim, confirm token minting is enabled and the team pool is an any-repo named team pool (not `default`).

Cursor never widens repository access beyond what the triggering user already has. If a run reaches the wrong checkout or cannot push, fix routing labels or worker git credentials rather than sharing a single broad service token across unrelated repos.

### What if I see rate limits?

[Contact support](https://cursor.com/help.md).

## How do I check if my team pool is at capacity?

Check worker capacity in the [Cloud Agents dashboard](https://cursor.com/dashboard/cloud-agents#self-hosted-agents). Team pool details and **My Machines** list workers by status.

For programmatic checks, call the summary API:

```bash
curl --request GET \
  --url "https://api.cursor.com/v0/private-workers/summary" \
  -u "$CURSOR_API_KEY:"
```

The response includes connected and in-use worker counts for your user and team.

Common reasons an agent run does not start:

- **No workers connected**: start or scale workers in the team pool, or confirm a My Machines worker is running
- **All workers busy**: requests wait in the team pool queue until a worker is free
- **Private worker limit exceeded**: your team hit the connected worker cap (200 per user, 1000 per team). Disconnect unused workers or [contact sales](https://cursor.com/contact-sales?source=docs-help-self-hosted) to discuss higher limits
- **Repository mismatch**: start the worker from the correct checkout or use an [any-repo team pool](https://cursor.com/help/ai-features/self-hosted-machines.md#can-i-use-a-team-pool-for-any-repository-without-specifying-one)

Workers send heartbeats while connected. A worker drops from the registry after it stops heartbeating. See [Team Pools](https://cursor.com/docs/cloud-agent/self-hosted/pool.md) for scaling and controller setup.

## Related

- [Cloud Agents](https://cursor.com/help/ai-features/cloud-agents.md)
- [Self-Hosted Machines](https://cursor.com/docs/cloud-agent/self-hosted.md)
- [My Machines](https://cursor.com/docs/cloud-agent/self-hosted/my-machines.md)
- [Team Pools](https://cursor.com/docs/cloud-agent/self-hosted/pool.md)
- [Integrations](https://cursor.com/docs/cloud-agent/self-hosted/integrations.md)
- [Computer use](https://cursor.com/docs/cloud-agent/self-hosted/computer-use.md)
- [Private connectivity](https://cursor.com/docs/cloud-agent/private-connectivity.md)
- [Cloud Agent security and network](https://cursor.com/docs/cloud-agent/security-network.md)


---

## Sitemap

[Overview of all docs pages](/llms.txt)
