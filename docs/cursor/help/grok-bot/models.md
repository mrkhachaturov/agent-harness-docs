# Which AI models power Grok Bot?

How Grok Bot chooses the model behind each request, what you see in your usage, how it affects your usage limits, and how it interacts with team model settings.

Grok Bot is not tied to a single model. For each task, it uses the backend model most likely to deliver the best outcome. That can be a first-party xAI model or a third-party model from a provider on the [sub-processor list](https://trust.cursor.com/subprocessors), and the choice can differ from one request to the next.

## Can I see which model handled a Grok Bot request?

No. Grok Bot does not show the underlying model for a request. Your usage and spending views record this activity as Grok Bot usage, not by provider or model name. See [What do the plan and spending screens call usage?](https://cursor.com/help/grok-bot/plans.md#what-do-the-plan-and-spending-screens-call-usage).

## Can I choose, request, or block a specific model in Grok Bot?

No. Grok Bot has no per-user or per-request model selection, and there is no model picker in [Grok Bot settings](https://cursor.com/docs/grok-bot/settings.md). Users cannot be routed to or away from a particular model. Grok Bot always uses the model most likely to produce the best result for the task.

## Does Grok Bot using Opus 5.5 cost more per token?

No. We work to give you the best price-performance and stretch your usage as far as possible. How fast you use it depends on the kind of work you give Grok Bot and how much effort each task takes, and routing a task to Opus 5.5 doesn't change what it costs you per token. To see where your usage went, open **Settings** > **Usage & Billing** in Grok Bot, or see [How does Grok Bot usage work?](https://cursor.com/help/grok-bot/plans.md#how-does-grok-bot-usage-work).

## Does my team's Cursor model allowlist apply to Grok Bot?

No. Grok Bot is not governed by your team's Cursor [model allowlist or blocklist](https://cursor.com/docs/enterprise/model-and-integration-management.md#model-access-control). It uses xAI first-party models and may use third-party models regardless of those settings. Teams with a model allowlist see this notice when they [enable Grok Bot](https://cursor.com/docs/grok-bot/teams.md#enabling-grok-bot-for-your-team). For data handling, see [Models and data](https://cursor.com/docs/grok-bot/security.md#models-and-data) on the Grok Bot security page.

## Which third-party providers can Grok Bot use?

Only providers on the [sub-processor list](https://trust.cursor.com/subprocessors). The set of models changes over time; the list is the authoritative reference for which providers may process your data.

## Related

- [Grok Bot Terms](https://cursor.com/terms/grok-bot)
- [Sub-processor list](https://trust.cursor.com/subprocessors)
- [Billing and payments](https://cursor.com/help/account-and-billing/billing.md)
- [Plans and billing](https://cursor.com/help/grok-bot/plans.md)
- [Grok Bot security](https://cursor.com/docs/grok-bot/security.md#models-and-data)


---

## Sitemap

[Overview of all docs pages](/llms.txt)
