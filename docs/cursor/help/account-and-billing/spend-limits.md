# Spend limits

Spend limits cap how much paid additional usage you're willing to pay for in a period. On [The X Subscription](https://cursor.com/help/the-x-subscription/overview.md) the control is a **monthly additional usage limit**. On [legacy Cursor plans](https://cursor.com/docs/account/pricing/legacy-cursor-plans.md) it's an on-demand **spend limit**. When a limit is reached, additional usage stops for that user until the limit is increased or the next period starts.

## How do I set a monthly additional usage limit on The X Subscription?

1. Go to [grok.com/dashboard/billing](https://grok.com/dashboard/billing)
2. Under **Additional usage credits**, find **Monthly additional usage limit** and click **Edit**
3. Enter an amount and save. Leave it unset for no cap

The limit counts paid additional usage you consume, not the prepaid credit you buy. Adding credit, manually or through Auto Top-up, doesn't count toward it, and buying more credit doesn't raise it. When you reach the limit, additional usage pauses until the next month or until you raise it, even if credit remains.

On Teams, admins set one limit for the whole team, either a fixed amount or an amount per seat. Only admins can change it or the Auto Top-up settings.

## How do I set a spend limit on a legacy Cursor plan?

1. Go to your [dashboard](https://cursor.com/dashboard/spending) under the **Spending** tab
2. On-demand usage must be enabled to view and set spend limits
3. Set a monthly spend limit for yourself or your team

Limit changes take effect immediately. Setting a limit to "No Limit" removes it. Raising a limit mid-cycle can make previously credited overage billable.

## Who can change spend limits?

On The X Subscription, only team admins can change the team's monthly additional usage limit and Auto Top-up settings.

On legacy Teams and Enterprise plans, whether team members can enable or disable on-demand usage and change the team-level spend limit depends on the **Only Admins Can Edit Usage Settings** toggle under **Permissions** in the [Spending tab](https://cursor.com/dashboard/spending):

- **When the toggle is off**, any team member can change these settings.
- **When the toggle is on**, only team admins can.

To restrict these controls to admins:

1. As a team admin, go to the [Spending tab](https://cursor.com/dashboard/spending)
2. Under **Permissions**, enable **Only Admins Can Edit Usage Settings**

Once enabled, team members can still view the Spending tab, but only admins can change on-demand usage and team-level limits. Member-level and group-level overrides on Enterprise plans are always admin-only.

Enterprise admins can review changes to this setting in the [audit log](https://cursor.com/docs/enterprise/compliance-and-monitoring.md#audit-logs) under the `admin_only_usage_pricing` event.

## What happens when a spend limit is reached?

- Paid additional usage stops for that specific user. Included weekly usage on The X Subscription keeps working
- Other team members continue unaffected
- The user sees a notification that their limit was reached
- Usage resumes automatically at the start of the next period

## What if usage goes over my spend limit?

Enforcement is not instant, so usage can briefly exceed your spend limit. Once we recognize that you have reached your spend limit, additional usage stops until you increase the limit or a new period starts. If a higher plan is available, upgrading can add included usage without raising the limit.

On legacy Cursor plans, we credit the limited overage that occurs prior to enforcement as a temporary spend-limit credit. That is not a refund or a permanent credit. You are billed up to your current limit. If you raise the limit in the same cycle, we may bill some or all of that credit, up to the new limit. Leave the limit unchanged, or turn off on-demand usage, to keep the credit.

## What types of spend limits are available?

**The X Subscription, individual plans:** Set a monthly additional usage limit for your own prepaid-credit usage.

**The X Subscription, Teams:** Admins set one monthly additional usage limit for the whole team, fixed or per seat.

**Legacy individual plans (Pro, Pro+, Ultra):** Set a monthly spend limit for your on-demand usage.

**Legacy Teams plans:** Set a team-level spend limit. When reached, all members consuming on-demand usage lose access to AI features.

**Enterprise plans:** Set both team-level and member-level limits. Member limits can be configured through:

1. Member overrides in the [Members tab](https://cursor.com/dashboard/members)
2. Group overrides in the [Groups tab](https://cursor.com/dashboard/members?subtab=active-directory)
3. Team general spend limit in the [Spending tab](https://cursor.com/dashboard/spending)

When a user has limits from multiple sources, Cursor applies the highest applicable limit. Enterprise admins can also manage limits through the [Admin API](https://cursor.com/docs/account/teams/admin-api.md#set-user-spend-limit).

## Does changing the team spend limit update existing member overrides?

No. Updating the team-level spend limit only changes the default for members who don't have a member or group override. Anyone with an existing override keeps their individual limit until you clear it.

To move a user back to the team default, remove their override in the [Members tab](https://cursor.com/dashboard/members) or [Groups tab](https://cursor.com/dashboard/members?subtab=active-directory). The same applies to limits set through the [Admin API](https://cursor.com/docs/account/teams/admin-api.md#set-user-spend-limit).

## What are dynamic spend limits?

Dynamic Spend Limits automatically adjust the team spend limit based on team size. As the number of seats grows or shrinks, the limit changes proportionally. Toggle this setting in the Spending tab.

## Do spend limits apply to pooled usage?

On Enterprise pooled usage accounts, member spend limits apply to total usage, not just on-demand.

## Related

- [Spend alerts](https://cursor.com/help/account-and-billing/spend-alerts.md)
- [Usage-based charges](https://cursor.com/help/account-and-billing/overages.md)
- [On-demand usage for mobile subscriptions](https://cursor.com/help/account-and-billing/on-demand-usage-for-mobile-subscriptions.md)
- [Usage and limits](https://cursor.com/help/models-and-usage/usage-limits.md)
- [Legacy Cursor plans](https://cursor.com/docs/account/pricing/legacy-cursor-plans.md)


---

## Sitemap

[Overview of all docs pages](/llms.txt)
