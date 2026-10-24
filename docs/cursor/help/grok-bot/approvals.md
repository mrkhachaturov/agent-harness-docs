# Approvals and Auto-review

Auto-review checks each action your Bot is about to take. Most actions run on their own. When one needs your OK, the Bot shows an approval card in your chat and waits for your answer.

## What is Auto-review?

Auto-review is a check that runs before the Bot acts, for example before it runs a command, uses a connected app, or uses its computer. It's on by default.

For each action, Auto-review either lets it run or has the Bot ask you first. Your Custom Rules can change that choice for the actions you care about. Built-in safety checks always apply, whatever your rules say.

## When does the Bot ask me first?

The Bot shows a card when Auto-review decides an action needs your OK. An action that matches one of your **Ask first** rules always gets a card.

Auto-review takes into account what you asked for in your own messages. Text from somewhere else, such as an email or a web page, doesn't count as your request.

Some cards carry a warning, such as **This can't be undone**, **This changes sign-in or security settings**, or **This shares your data outside this chat**.

For email the Bot sends from its own address:

- When you ask for an email in chat, it goes out once Auto-review allows it. If Auto-review needs you, you see an approval card first.
- Email from a routine, an incoming message, or other work you didn't start with that request waits as a draft until you press **Send**.
- A forward, or an email with an attachment Auto-review can't fully read, always waits for your OK.

See [Does my Bot need my approval to send email?](https://cursor.com/help/grok-bot/agent-email.md#does-my-bot-need-my-approval-to-send-email)

## What do the buttons on an approval card do?

- **Allow once**: the Bot does the action now. No rule is saved.
- **Always allow**: the Bot does the action now and saves an Allow rule to your Custom Rules, so similar actions run on their own. The card shows **Saved to Custom Rules**.
- **Deny**: the Bot doesn't do it. It won't try that action again or ask you about it until you send another message.

Some cards use other labels:

- A card for a terminal command shows **Allow** and **Skip**. It also has **Manage settings**, which opens your Auto-review settings.
- A card paused by one of your **Ask first** rules shows **Allow** and **Not now**.
- When the card has no rule to offer, you see **Allow** instead of **Allow once**, and no **Always allow**.

On the phone, tap a card to see the full request and all of its buttons.

## What happens if I don't answer?

It depends on how the work started:

- When the work started from a chat message, the card waits for an answer. It doesn't expire on a timer.
- When a routine, an incoming message, or other background work raised the card, it expires after 30 minutes.

If you send a new message instead of answering, any open card in that chat closes. Changing your Auto-review settings also closes open cards.

A closed card shows **Expired** and says the Bot didn't do the action. If the card offered a rule, you can still press **Always allow next time**. The Bot saves the rule and can go ahead the next time.

## Where do I find Custom Rules?

On desktop, open **Settings** > **General** and go to the **Bot** section. **Custom Rules** appears under the **Auto-review** switch while Auto-review is on.

On the phone, open **Settings**, find the **Bot** group, and tap **Custom Rules**.

When a card was paused by one of your rules, press **Edit rule** on the card to open your Custom Rules.

## How do I write a rule?

1. Under **When Grok Bot wants to:**, describe one action in plain words, like "reply to emails for me".
2. Under **It should:**, choose **Allow automatically** or **Ask first**.
3. Press **Add Rule**.

Write one short rule for each action. If two rules conflict, **Ask first** wins.

On the phone, tap **Add Rule** on the **Custom Rules** screen. The choices there are **Allow Automatically** and **Ask First**.

## How many rules can I have?

You can have up to 20 **Allow automatically** rules and up to 20 **Ask first** rules. Each rule can be up to 1,000 characters.

If you already have 20 Allow rules, **Always allow** on a card removes your oldest Allow rule to make room. The card tells you which rule it removed.

## How do I edit or delete a rule?

On desktop, use the edit button next to a rule, make your change, and press **Save Rule**. Press **Cancel** to keep the rule as it was. Use the delete button next to a rule to remove it.

On the phone, tap a rule to open it. Press **Save Rule** to keep your change, or **Delete Rule** to remove it.

## What does "Required by your admin" mean?

If you're on a team, your admin can set Auto-review for you:

- If your admin requires Auto-review, its switch stays on and shows **Required by your admin. You can't turn this off.**
- Team rules show **Required by your admin. You can't edit or delete this rule.** Team rules always apply. Your own rules apply only to you.
- Your team can also share rules that apply to your Bots instead of your own rules. Built-in safety checks still apply.

## How do I turn Auto-review off?

On desktop, open **Settings** > **General** and turn off the **Auto-review** switch in the **Bot** section. On the phone, turn off **Auto-review** in the **Bot** group of **Settings**.

With Auto-review off, the Bot runs actions without checking them first. Your Custom Rules are hidden and not used, but they're kept. Turn Auto-review back on to use them again.

## How do approvals work on Team Bots and group chats?

On a Team Bot, each teammate answers cards for their own requests in their own chat with the Bot. In a Slack thread, the card has **Allow once**, **Deny**, and **View details**, and only the person who asked can answer. See [Team Bots](https://cursor.com/help/grok-bot/team-bots.md).

In a group chat, only the person whose message the Bot is answering can approve. Everyone else sees who the card is waiting on. Group chat cards don't offer **Always allow**.

## How is this different from Secure Forms and connect cards?

An approval card asks whether the Bot may take an action. Two other cards look similar but do different jobs:

- A Secure Form collects a password, key, or other secret and saves it to the Bot's vault. See [Store secrets securely](https://cursor.com/help/grok-bot/secrets.md).
- A connect card asks you to sign in to an app so the Bot can use it. See [Connect apps](https://cursor.com/help/grok-bot/connect-apps.md).

## Related

- [Team Bots](https://cursor.com/help/grok-bot/team-bots.md)
- [Group chats and Bot-to-Bot messages](https://cursor.com/help/grok-bot/group-chats.md)
- [Give your Bot an email address](https://cursor.com/help/grok-bot/agent-email.md)
- [Grok Bot How Tos](https://cursor.com/help/grok-bot/how-to.md)


---

## Sitemap

[Overview of all docs pages](/llms.txt)
