# Give your Bot an email address

You can claim an email address for your Bots at `mail.grokbot.com`, such as `yourname@mail.grokbot.com`. Your Bots can then receive, read, search, and send email from it.

With an address, a Bot can:

- Sign up for services with its own address, and pick up the verification code or link with your OK.
- Collect receipts, newsletters, and reports, and summarize them for you.
- Send email for you, such as a digest or an update, and handle replies, once you've asked it to.
- Run a routine when email arrives, optionally only from specific senders.

## How do I get an email address for my Bot?

You can claim it two ways:

- **Ask your Bot.** Say something like "Get yourself an email address." The Bot asks what name you want, checks that it's free, and shows an approval card. Nothing is claimed until you approve.
- **Use the Email plugin.** On desktop, open the plugin marketplace from the sidebar and choose **Email**. On the phone, open **Settings** > **Plugins** > **Email**. Under **Email address**, type a name in **Choose a name**, then choose **Create address**.

After you claim it, the plugin shows your address with a button to copy it.

If you use Grok Bot through a Cursor team, a team admin has to turn on agent email first. See [How do team admins turn on agent email?](https://cursor.com/help/grok-bot/agent-email.md#how-do-team-admins-turn-on-agent-email)

## What names can I choose?

- Use lowercase letters, digits, dots, hyphens, and underscores.
- Start and end with a letter or digit.
- Use at most 64 characters.
- Avoid reserved words such as support, admin, billing, security, help, info, team, cursor, grok, and xai.

Every address is unique. Once someone claims an address, it's never given to anyone else, even after the account that claimed it is deleted.

## Can I have more than one address, or change mine?

You can have one address. You can't rename it or delete it, so choose the name carefully.

## Which of my Bots can use my address?

The address belongs to you, not to one Bot. All of your Bots can use it in your own chats with them, and in routines you set up.

Bots can't use your address in Slack threads or in chats where someone else is talking to the Bot. A [Team Bot](https://cursor.com/help/grok-bot/team-bots.md) doesn't have a shared team address.

## Who can email my Bot, and where do I see the mail?

Anyone can send email to your address. Mail that fails the spam or virus scan is kept without its body or attachments, and it never starts a routine.

There's no inbox view in the apps, and you don't get notifications for new mail. To see your mail, ask your Bot, for example "What arrived in your inbox today?" or "Find the receipt from last week." Mail that arrived in the last minute may not show up in a search yet.

Each message can include up to 10 attachments, up to 10 MB each and 25 MB in total. Attachments beyond those limits are skipped.

## How do I have my Bot act on incoming email?

Set up a routine. New mail doesn't start a chat or wake a Bot on its own. A Bot acts on incoming mail only through a routine you create.

Ask your Bot in chat, for example "When an email arrives from [billing@example.com](mailto:billing@example.com), summarize it and tell me." A routine can watch for:

- Mail from anyone.
- Mail from specific addresses, such as `billing@example.com`.
- Mail from a whole domain, such as `*@example.com`.

By default, the routine only runs for mail from senders that pass standard email authentication checks. Routines can't filter by subject. See [Routines](https://cursor.com/help/grok-bot/routines.md).

## Does my Bot need my approval to send email?

Yes. Your Bot sends email only when you've asked it to, either in chat or in a routine's instructions. Otherwise it shows you the full draft and asks first. Replying counts as sending.

If **Auto-review** is on, sends are checked the same way as other actions, and some sends always ask you. Instructions inside an email the Bot received never count as your permission to send.

If you've also connected Gmail or Outlook, your Bot asks which account to send from when either could work.

## Are there limits on what my Bot can send?

- Up to 50 recipients per email, across To, Cc, and Bcc.
- Up to 10 attachments, up to 10 MB each and 25 MB in total. Executable files can't be attached.
- Newsletters and first-contact emails go to one recipient per message and include a one-click unsubscribe link.
- If a message bounces, or someone unsubscribes or marks it as spam, your Bot stops emailing that address and tells you who it skipped.

There are also limits on how many new people a Bot can email, to protect the address from being flagged as spam.

## How is email content kept safe?

Your Bot treats email from other people as information, not instructions. Each message it reads is marked as from you or from someone else, and a request inside an email doesn't make it send anything or take other actions on its own.

If you delete your Grok Bot account, your mail and attachments are deleted. The address itself is retired and never given to anyone else. See [Delete your Grok Bot account](https://cursor.com/help/grok-bot/delete-account.md).

## How do team admins turn on agent email?

For Cursor teams, agent email is off by default. A team admin turns it on in the [Cursor dashboard](https://cursor.com/dashboard/bot): on the **Grok Bot** page, under **Bot Capabilities**, turn on **Agent Email**. Members can then claim an address.

If an admin turns agent email off later, Bots lose their email tools and email routines stop running. Mail sent to existing addresses is still received and kept, and members keep their addresses.

## Why can't I claim an address?

| What you see                                                                                                         | What to do                                                                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Agent email is not enabled for this account.**                                                                     | Agent email isn't available on your account yet.                                                                                                                                      |
| **Your team admin has turned off Grok Bot agent email, so this account cannot claim or use an agent email address.** | Ask your team admin to turn on **Agent Email**. See [How do team admins turn on agent email?](https://cursor.com/help/grok-bot/agent-email.md#how-do-team-admins-turn-on-agent-email) |
| **That address is taken, and addresses are never reissued, so retrying it cannot succeed. Choose a different name.** | Choose a different name.                                                                                                                                                              |
| A message about allowed characters, length, or a reserved word                                                       | Pick a name that follows [the name rules](https://cursor.com/help/grok-bot/agent-email.md#what-names-can-i-choose).                                                                   |
| **You can have one agent email address.**                                                                            | You already have an address. Ask your Bot what it is, or open the **Email** plugin.                                                                                                   |
| **Couldn't create your email address. Try again.** (phone)                                                           | Check the [name rules](https://cursor.com/help/grok-bot/agent-email.md#what-names-can-i-choose), or try on desktop, which shows the exact reason.                                     |
| **Too many email addresses checked in the last minute.**                                                             | Wait a minute, then try again.                                                                                                                                                        |

If none of these match, [contact support](https://cursor.com/help/grok-bot/get-help.md) with your Cursor account email and the exact message.

## Related

- [Routines](https://cursor.com/help/grok-bot/routines.md)
- [Connect plugins](https://cursor.com/help/grok-bot/connect-plugins.md)
- [Team Bots](https://cursor.com/help/grok-bot/team-bots.md)
- [Grok Bot for Teams and Enterprise](https://cursor.com/docs/grok-bot/teams.md)


---

## Sitemap

[Overview of all docs pages](/llms.txt)
