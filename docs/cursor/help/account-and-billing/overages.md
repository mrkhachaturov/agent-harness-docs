# Usage-based charges

If you see charges beyond your base subscription, you likely have on-demand usage enabled.

## How does on-demand pricing work?

Each plan includes a monthly usage budget. If you exceed your included usage, additional requests are billed at API rates with no markup.

On Teams and Enterprise plans, third-party model requests also include the [Cursor Token Rate](https://cursor.com/help/models-and-usage/token-rate.md). This includes when Auto routes to a third-party model. First-party Cursor models, including Grok and Composer, are exempt.

- On-demand usage must be explicitly enabled in your settings
- On-demand usage has its own invoices and line items, distinct from your subscription

## How do I check my usage?

Go to [cursor.com/dashboard](https://cursor.com/dashboard) and click **Billing & Invoices**. You'll see two sections:

- **Included Usage**: Usage covered by your monthly subscription.
- **On-Demand Usage**: Any usage charged above your monthly subscription.

## How do I prevent on-demand charges?

- **Disable on-demand usage**: Turn it off in your dashboard settings to stop requests once your included usage runs out
- **Set a spend limit**: Cap how much on-demand usage you're willing to pay that billing cycle. Raising it mid-cycle can make previously credited overage billable.
- **[Upgrade your plan](https://cursor.com/help/account-and-billing/pricing.md#how-do-i-upgrade-my-plan)**: Pro+ or Ultra give you higher included usage limits for Cursor Models and Other Models.

## What if usage goes over my spend limit?

Enforcement is not instant, so usage can briefly exceed your spend limit. Once we recognize that you have reached your spend limit, on-demand usage stops until you increase the spend limit or a new billing cycle starts. If a higher plan is available, upgrading can add included usage without raising the spend limit.

We will credit the limited overage that occurs prior to enforcement as a temporary spend-limit credit. That is not a refund or a permanent credit. You are billed up to your current limit. If you raise the limit in the same cycle, we may bill some or all of that credit, up to the new limit. Leave the limit unchanged, or turn off on-demand usage, to keep the credit.

## Why did my usage costs increase after the Cursor Router launch?

Cursor Router introduced new Auto optimization modes. All Auto modes bill at the routed model's list price.

If you were using the former Auto mode before the launch, you will be defaulted to Auto **Cost** mode.

See [Cursor Router](https://cursor.com/help/models-and-usage/cursor-router.md) for mode details and [pricing and plans](https://cursor.com/help/account-and-billing/pricing.md#why-is-the-old-auto-mode-now-called-cost-mode) for the Cost rename.

## Related

- [Cursor Router](https://cursor.com/help/models-and-usage/cursor-router.md)
- [Usage and limits](https://cursor.com/help/models-and-usage/usage-limits.md)
- [Spend limits](https://cursor.com/help/account-and-billing/spend-limits.md)
- [Pricing and plans](https://cursor.com/help/account-and-billing/pricing.md)
- [Billing and payments](https://cursor.com/help/account-and-billing/billing.md)
- [Invoices](https://cursor.com/help/account-and-billing/invoices.md)


---

## Sitemap

[Overview of all docs pages](/llms.txt)
