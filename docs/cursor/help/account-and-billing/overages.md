# Usage-based charges

If you see charges beyond your base subscription, they're for additional usage: top-ups on [The X Subscription](https://cursor.com/help/the-x-subscription/overview.md), or on-demand usage on a [legacy Cursor plan](https://cursor.com/docs/account/pricing/legacy-cursor-plans.md).

## How do top-ups work on The X Subscription?

Top-ups add prepaid credit to your subscription. Credit pays for:

- **Third-party models** in Cursor, like Claude or GPT, from the first request. They aren't part of your included weekly pool. Premium and above only.
- **Cursor models beyond your weekly pool**, at the same per-model rates as included usage.

You're charged when you buy credit or when an automatic top-up runs, not in arrears.

- **Manual top-up:** buy credit whenever you choose under **Additional usage credits** at [grok.com/dashboard/billing](https://grok.com/dashboard/billing).
- **Auto Top-up:** off until you turn it on. When it's on, it charges your saved payment method and adds the amount you chose whenever your balance drops below your threshold.
- **Teams:** the team shares one prepaid balance. Only admins can buy credit or change Auto Top-up.
- Top-up charges appear under **Billing & invoices** › **Invoices** at [grok.com/dashboard/billing](https://grok.com/dashboard/billing), separate from your subscription charge.

On Teams and Enterprise plans, third-party model requests also include the [Cursor Token Rate](https://cursor.com/help/models-and-usage/token-rate.md). This includes when Cursor Router (Balance or Intelligence) routes to a third-party model. Cost mode requests and Cursor models, including Grok and Composer, are exempt.

## How does on-demand pricing work on legacy Cursor plans?

Each legacy plan includes a monthly usage budget. If you exceed your included usage, additional requests are billed at API rates with no markup, in arrears each month.

- **Individual plans (Pro, Pro+, Ultra):** On-demand usage must be explicitly enabled in your settings.
- **Teams Standard and Premium:** On-demand usage is enabled by default. Team admins can disable it or set spend limits in the dashboard.
- On-demand usage has its own invoices and line items, distinct from your subscription.
- Third-party requests on Teams and Enterprise also include the [Cursor Token Rate](https://cursor.com/help/models-and-usage/token-rate.md).

## How do I check my usage?

- **The X Subscription:** open **Usage** at [grok.com/dashboard](https://grok.com/dashboard) for your weekly pool, and **Additional usage credits** at [grok.com/dashboard/billing](https://grok.com/dashboard/billing) for your prepaid credit and what it's been spent on.
- **Legacy Cursor plans:** go to [cursor.com/dashboard](https://cursor.com/dashboard) and click **Billing & Invoices**. You'll see **Included Usage**, covered by your subscription, and **On-Demand Usage**, charged above it.

## How do I prevent additional charges?

**On The X Subscription:**

- **Leave Auto Top-up off**, or turn it off under **Additional usage credits** at [grok.com/dashboard/billing](https://grok.com/dashboard/billing). Additional usage then stops once your weekly pool and any credit you already bought are used up. Credit you've already bought stays available until used or until it expires (currently 365 days after purchase).
- **Set a monthly additional usage limit**: Cap how much paid additional usage you can consume each month. When you reach it, additional usage pauses until next month or until you raise the limit, even if credit remains. See [Spend limits](https://cursor.com/help/account-and-billing/spend-limits.md).
- **Use Cursor models**: Grok and Composer draw from your included pool instead of prepaid credit.
- **[Upgrade your plan](https://cursor.com/help/account-and-billing/pricing.md#how-do-i-change-plans-on-the-x-subscription)**: Super and Ultra include larger weekly pools.

**On a legacy Cursor plan:**

- **Disable on-demand usage**: On individual plans, turn it off in your spending settings to stop requests once your included usage runs out. On Teams, admins disable it in the team dashboard.
- **Set a spend limit**: Cap how much on-demand usage you're willing to pay that billing cycle. On individual plans, set this in your spending settings. On Teams, admins set it in the team dashboard. Raising it mid-cycle can make previously credited overage billable.
- **[Upgrade your plan](https://cursor.com/help/account-and-billing/pricing.md#how-do-i-change-plans-on-a-legacy-cursor-plan)**: Pro+ or Ultra give you higher included usage limits for Cursor Models and Other Models.

## What if usage goes over my spend limit?

Enforcement is not instant, so usage can briefly exceed your spend limit. Once we recognize that you have reached your spend limit, additional usage stops until you increase the limit or a new period starts. If a higher plan is available, upgrading can add included usage without raising the limit.

On legacy Cursor plans, we credit the limited overage that occurs prior to enforcement as a temporary spend-limit credit. That is not a refund or a permanent credit. You are billed up to your current limit. If you raise the limit in the same cycle, we may bill some or all of that credit, up to the new limit. Leave the limit unchanged, or turn off on-demand usage, to keep the credit.

## Why did my usage costs increase after the Cursor Router launch?

Cursor Router introduced new Auto optimization modes. On Teams and Enterprise with Cursor Router on, Balance and Intelligence bill at the routed model's list price, including third-party models. Cost mode keeps billing as a Cursor-model request.

If you were using the former Auto mode before the launch, you will be defaulted to Auto **Cost** mode.

See [Cursor Router](https://cursor.com/help/models-and-usage/cursor-router.md) for mode details and [pricing and plans](https://cursor.com/help/account-and-billing/pricing.md#why-is-the-old-auto-mode-now-called-cost-mode) for the Cost rename.

## Related

- [Cursor Router](https://cursor.com/help/models-and-usage/cursor-router.md)
- [Usage and limits](https://cursor.com/help/models-and-usage/usage-limits.md)
- [Spend limits](https://cursor.com/help/account-and-billing/spend-limits.md)
- [Team Pricing](https://cursor.com/docs/account/teams/pricing.md)
- [Legacy Cursor plans](https://cursor.com/docs/account/pricing/legacy-cursor-plans.md)
- [On-demand usage for mobile subscriptions](https://cursor.com/help/account-and-billing/on-demand-usage-for-mobile-subscriptions.md)
- [Pricing and plans](https://cursor.com/help/account-and-billing/pricing.md)
- [Billing and payments](https://cursor.com/help/account-and-billing/billing.md)
- [Invoices](https://cursor.com/help/account-and-billing/invoices.md)


---

## Sitemap

[Overview of all docs pages](/llms.txt)
