# GitHub, GitLab, Azure DevOps, and Bitbucket

Connect GitHub, GitLab, Azure DevOps, or Bitbucket Cloud to use Cloud Agents. GitHub, GitLab, Azure DevOps, Bitbucket Cloud, and Bitbucket Data Center also support Bugbot.

Azure DevOps and Bitbucket Cloud are in public beta.

## How do I connect GitHub?

Follow the setup steps in the [GitHub integration docs](https://cursor.com/docs/integrations/github.md). Both GitHub.com and GitHub Enterprise Server are covered.

Once connected, you can run [Bugbot](https://cursor.com/help/ai-features/bugbot.md) on your pull requests and trigger [Cloud Agents](https://cursor.com/agents) from your repos.

## How do I connect GitLab?

Follow the setup steps in the [GitLab integration docs](https://cursor.com/docs/integrations/gitlab.md). Both GitLab.com and self-hosted instances are covered.

Once connected, you can run [Bugbot](https://cursor.com/help/ai-features/bugbot.md) on your merge requests and trigger [Cloud Agents](https://cursor.com/agents) from your repos.

## Why do older GitLab merge requests from Cursor show Ghost User?

Cloud Agents commit and open merge requests as the bot user of the project access token Cursor creates for each project. When Cursor replaces a project's token, it revokes the old one. GitLab then removes the old token's bot user (after 30 days on GitLab 17.9 and later) and moves its merge requests and comments to a ghost user, shown as Ghost User on GitLab.com. See [GitLab commit author](https://cursor.com/docs/integrations/gitlab.md#commit-author).

## What if a GitLab pipeline can't include another project's CI file after a Cloud Agent push?

Pipelines triggered by an agent's push run as the project's bot user. GitLab doesn't let a project access token's bot user join other projects, so an `include:project` from another private project returns a `not found or access denied` error. To run it, start a new pipeline for the agent's branch yourself (for example, with **Run pipeline**) as a member of both projects.

## How do I connect Azure DevOps?

Follow the setup steps in the [Azure DevOps integration docs](https://cursor.com/docs/integrations/azure-devops.md). Azure DevOps Services at `dev.azure.com` is covered.

Once connected, you can run [Bugbot](https://cursor.com/help/ai-features/bugbot.md) on your Azure DevOps pull requests and trigger [Cloud Agents](https://cursor.com/agents) from your repos.

## How do I connect Bitbucket?

Follow the setup steps in the [Bitbucket integration docs](https://cursor.com/docs/integrations/bitbucket.md). Cursor supports Bitbucket Cloud repositories on `bitbucket.org` and self-hosted Bitbucket Data Center instances.

Both deployment types support [Bugbot](https://cursor.com/help/ai-features/bugbot.md). Bitbucket Cloud also supports [Cloud Agents](https://cursor.com/agents).

## How do I connect a private or self-hosted GitLab instance with Self-Hosted Machines?

Use an any-repo team pool on a worker that can reach your GitLab instance over your network. See [Self-Hosted Machines](https://cursor.com/help/ai-features/self-hosted-machines.md#how-do-i-connect-private-or-self-hosted-gitlab) for setup steps.

## Related

- [GitLab integration](https://cursor.com/docs/integrations/gitlab.md)
- [Cloud Agents](https://cursor.com/help/ai-features/cloud-agents.md)


---

## Sitemap

[Overview of all docs pages](/llms.txt)
