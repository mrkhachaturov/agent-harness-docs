# Usage and limits

Most Cursor plans include two monthly usage pools:

- **Cursor Models**: Grok 4.7, Grok 4.6, Grok 4.5, and Composer 2.5
- **Other Models**: Third-party models, charged at model provider prices

Pro, Pro Plus, and Ultra include both pools. The Start plan covers the Cursor Models pool only. See [Cursor Start](https://cursor.com/help/account-and-billing/cursor-start.md) for India plan details.

Your model selection affects how quickly your included usage is consumed.

Current usage-based plans don't include Max Mode. On legacy request-based plans, [Max Mode](https://cursor.com/help/ai-features/max-mode.md) is billed at the model's API rate plus 20%.

## How do I check my usage?

Go to the [Spending](https://cursor.com/dashboard/spending) tab in your dashboard. It shows real-time usage for both pools, remaining allowance, and any on-demand charges.

## What happens when I hit my usage limit?

You'll see a notification in the editor. You can either enable on-demand usage (pay-as-you-go) or upgrade to a higher plan.

## When does my usage reset?

Usage resets monthly with your billing cycle. Unused usage does not roll over. The reset date is shown on the [Spending](https://cursor.com/dashboard/spending) tab.

For teams, all members' usage resets at the same time based on the team billing cycle.

## How do I get more usage?

- **Use Cursor Models**: Grok 4.7, Grok 4.6, Grok 4.5, and Composer 2.5 draw from the Cursor Models pool, tracked separately and included with your plan
- **Enable on-demand usage**: Pay for additional requests at the same API rates
- **[Upgrade your plan](https://cursor.com/help/account-and-billing/pricing.md#how-do-i-upgrade-my-plan)**: Higher-tier plans include more usage

## How does Cursor Router interact with my plan's usage pools and limits?

Cursor Router requests are billed at the routed model's cost and can draw from both the Cursor Models pool and the third-party Other Models pool, depending on which model handles the request.

- **Composer 2.5** requests carry no [Cursor Token Rate](https://cursor.com/help/models-and-usage/token-rate.md) on any plan
- All Auto modes bill at the routed model's list price. Third-party models also incur the Cursor Token Rate

When included usage runs out, on-demand charges apply if you have on-demand usage enabled. Check your [Spending dashboard](https://cursor.com/dashboard/spending) for request-level cost and pool details.

See [Cursor Router](https://cursor.com/help/models-and-usage/cursor-router.md) for mode details.

## Do requests made with my own API key count toward my usage?

On individual plans, no. Your provider bills you directly for the model cost, and those requests don't draw from either pool.

On Teams and Enterprise plans, requests made with your own key still carry the [Cursor Token Rate](https://cursor.com/help/models-and-usage/token-rate.md) of $0.25 per million tokens. That charge appears under **Other Models** and draws from that allowance. When the allowance runs out, the Cursor Token Rate is billed as on-demand usage if on-demand usage is enabled. If it is turned off, those requests stop until the next billing cycle.

See [Bring your own API key](https://cursor.com/help/models-and-usage/api-keys.md#does-using-my-own-api-key-count-against-my-included-usage) for details.

## Related

- [Cursor Router](https://cursor.com/help/models-and-usage/cursor-router.md)
- [Pricing and plans](https://cursor.com/help/account-and-billing/pricing.md)
- [Usage-based charges](https://cursor.com/help/account-and-billing/overages.md)
- [Available models](https://cursor.com/help/models-and-usage/available-models.md)
- [API keys](https://cursor.com/help/models-and-usage/api-keys.md)
- [Pricing reference](https://cursor.com/docs/models-and-pricing.md)
- [Model pricing](https://cursor.com/docs/models-and-pricing.md#model-pricing)


---

## Sitemap

[Overview of all docs pages](/llms.txt)
