# Shared Bots

A Bot is either personal or shared. Share a Bot the way you'd share a doc: with your Cursor team, your whole organization, or only certain people and groups. Sharing doesn't make a copy, and each person's chat with a shared Bot is private.

Shared Bots always run in the cloud. A Bot that runs on your own computer can't be shared. The app still says **Team Bots** in Settings and in a few messages. They're the same thing.

## Who can use shared Bots?

Shared Bots are for members of a Cursor team who have Grok Bot. Choose **+** in the sidebar to see **Create a Bot** and **Browse shared Bots**. If **Browse shared Bots** isn't there, you aren't on a Cursor team, or your Grok Bot app needs an update.

In Slack, members of your workspace who aren't on the team can sometimes use a shared Bot too. See [Who can talk to a shared Bot in Slack?](https://cursor.com/help/grok-bot/shared-bots.md#who-can-talk-to-a-shared-bot-in-slack)

## How do I create a Bot for my team?

1. Choose **+** in the sidebar, then **Create a Bot**, and give it a name.
2. Tell the Bot what it should help the team with. A sentence is enough.
3. Follow its setup steps for apps, secrets, skills, and files. Only add keys and files you're happy for everyone you share it with to use. Until you publish it, it's a draft only you can see.
4. When the Bot says it's ready to share, choose **Publish**. Teammates can then find it. To change who has access, see [How do I share a Bot with my team?](https://cursor.com/help/grok-bot/shared-bots.md#how-do-i-share-a-bot-with-my-team)

You can also share a Bot you already have. Sharing doesn't duplicate it. Before you share, check its apps, secrets, skills, and files, since they work in every teammate's chat.

## How do I share a Bot with my team?

Click the Bot's name at the top of the chat and choose **Share**. In **Share this Bot**:

- Under **Who has access**, choose **Only you**, **People you invite**, your team, or your organization. **People you invite** shares the Bot only with the people and groups you add. Limiting access asks you to confirm with **Limit access**. The owner and Managers can always use the Bot.
- Choose **Add people or groups** to add someone. Under **Add as**, pick **Collaborator** to let them chat with the Bot, or **Manager** to let them also change how it works: its instructions, skills, memory, and apps.
- Choose **Copy link** to send teammates a link to the Bot.

To stop sharing, open **Share** again and choose **Only you**, or remove people's access.

## Who can share Bots?

Anyone on the team, unless an admin changes it. On the Grok Bot page of the team dashboard, **Bot sharing** under **Sharing** is set to **Everyone** or **Admins only**. With **Admins only**, **Share** is disabled for members and shows **Only team admins can share Bots**. Bots that were already shared stay shared, and their owners and Managers can still use them. Ask an admin to share a Bot for you, or to change the setting. See [How do admins manage shared Bots?](https://cursor.com/help/grok-bot/shared-bots.md#how-do-admins-manage-shared-bots)

## How do teammates find a shared Bot?

- Choose **+** in the sidebar, then **Browse shared Bots**. The list shows Bots shared with you, and each one shows who made it. Choose **Add** to keep a Bot in your sidebar.
- Press Cmd+K on Mac or Ctrl+K on Windows and choose **Browse shared Bots**. The list starts with **Popular** Bots, and you can search it.
- Ask your Bot which shared Bot can help with something. It searches the shared Bots you can use and recommends ones you haven't opened.
- On your phone, tap **+**, then **Browse shared Bots**.
- Open a link a teammate sent you, then choose **Start a chat**.

A shared Bot's link opens the same Bot for everyone. It's different from [sharing a Bot template](https://cursor.com/docs/grok-bot/work.md#share-a-bot), which gives each person their own copy.

## Can the owner see my chats with a shared Bot?

No. Each person's chat with a shared Bot is private. The owner and Managers can't read your chats, and you can't read the owner's or anyone else's.

The Bot can learn things for the whole team. What it learns from a teammate waits until the owner or a Manager approves it under **Review learnings**. It doesn't save anything about you personally for the team. What it remembers about working with you stays between you and the Bot. See [What does a shared Bot learn for the team?](https://cursor.com/help/grok-bot/memory.md#what-does-a-shared-bot-learn-for-the-team)

## Whose apps and secrets does a shared Bot use?

A shared Bot uses the apps and secrets its owner added. Those work the same for everyone who chats with it.

In your own chat with a shared Bot, it can also use your apps. It asks before it uses one of your personal accounts. The card says **Allow**, then the app name:

- **Allow once** lets it use that account this time.
- **Always allow** remembers your answer. Its menu has **Always allow for your messages to this Bot** and **Always allow for your messages to every Team Bot**.
- **Skip** means it doesn't use that account this time.

In Slack channels, threads, and group chats, a shared Bot uses only its owner's apps, and asks before it uses your accounts.

A connected account acts as the person the Bot is answering. One teammate's connection is never used for someone else, unless a Manager shares it as a shared connector.

To make every shared Bot ask again, open **Settings** > **General** > **Team Bots** and choose **Clear** next to **Clear connector preferences**.

## How do shared connectors work?

A shared connector lets everyone use an app through one account, so teammates don't each have to connect it. The owner or a Manager sets it up: open the Bot's details and, under **Setup**, choose **Service accounts**. Pick an app under **Shared connectors**, then choose how the Bot signs in to it:

- **Use individual accounts**: each teammate connects their own.
- **Share your account**: everyone who uses the Bot acts through your account, including to make changes. Connect the app for yourself first, and only share an account that holds nothing sensitive or private.
- The Bot's own account: a separate account the Bot uses for the team. Some apps don't support this yet.

Sharing your account needs a team admin to turn on **Allow Shared Logins** first. Until then, the Bot says **Your admin has turned off sharing logins with Bots**. See [How do admins manage shared Bots?](https://cursor.com/help/grok-bot/shared-bots.md#how-do-admins-manage-shared-bots)

The app's row shows whose account the Bot uses. To stop, choose **Stop sharing**, or remove the app. Teammates then connect their own.

## Which computer does a shared Bot use?

In your own chat with a teammate's shared Bot, the Bot usually works on your Grok Bot computer. That means it can use the files there and the sites you're signed in to there. Sometimes it uses a separate computer just for that conversation, for example when your privacy mode is stricter than the owner's.

When you DM a shared Bot in Slack, it also works on your own computer. In Slack channels, threads, group DMs, and group chats, a shared Bot uses one shared computer of its own.

## Whose usage pays for a shared Bot chat?

A shared Bot reply uses the Grok Bot usage of the person it's answering. That's true in your own chat, in Slack, and in group chats. Your own limits apply. The owner's usage pays for the owner's own messages, and for Slack posts from apps or workflows that aren't linked to a Cursor account. A reply to someone in Slack who hasn't linked an account or isn't on the team uses the team's usage. See [Plans and billing](https://cursor.com/help/grok-bot/plans.md).

## How do approvals work on a shared Bot?

A shared Bot asks the person it's answering before risky actions.

- In your own chat with a shared Bot, you answer its approval cards.
- In a Slack thread, the Bot posts a **Review an action** card with **Allow once**, **Deny**, and **View details**. Only the person who asked can answer it.
- In a group chat, only the person whose message the Bot is answering can answer.

It also asks before it uses your personal accounts. See [Whose apps and secrets does a shared Bot use?](https://cursor.com/help/grok-bot/shared-bots.md#whose-apps-and-secrets-does-a-shared-bot-use)

## How do I add a shared Bot to Slack?

The owner or a Manager adds it, after sharing:

1. Click the Bot's name at the top of the chat.
2. Find **Bring to your team's Slack** and choose **Connect**.
3. If it says **Awaiting admin approval**, a Slack workspace admin needs to approve the app.

Once it says **Connected**, teammates can message the Bot directly or mention it in channels.

In a channel thread or a DM, the shared Bot acts for the teammate who mentioned it. It can hand work to that person's own Bots, and their replies are posted back into the same thread. A personal Bot doesn't hand work to other Bots from a channel thread. See [Can a Bot message other Bots from Slack?](https://cursor.com/help/grok-bot/group-chats.md#can-a-bot-message-other-bots-from-slack)

Bots record who asked for each message they post in Slack, so anyone in the thread can ask the Bot who requested it. When a shared Bot's routine replies in a Slack thread, the Bot follows that thread and answers later replies without an @mention.

Link your Slack account so the Bot knows who you are and can use your apps. Open **Settings** > **General** > **Team Bots** and choose **Link**.

## Who can talk to a shared Bot in Slack?

It depends on who the Bot is shared with.

- **Your organization**: any full member of your Slack workspace can mention it in channels and threads, even without a linked Cursor account or a seat on your team. Without a linked account, they're told once per thread that **some features will be limited**. In a DM, they still need to link first. The same goes for a Bot shared with your team when the team isn't in an organization, or is the only team in it.
- **Your team, or certain people**: only people it's shared with. A linked teammate without access is told the Bot **hasn't been shared with you yet**. Add them under **Share this Bot**. Someone without a linked account is asked to link one.
- **A personal Bot** only chats with its owner.

Slack guests, Slack Connect channels, and other Slack workspaces are never included. If your Slack email matches a Cursor account that already has access, the Bot asks you to link it instead.

A team admin can turn this off for workspace members who aren't on the team. See [How do admins manage shared Bots?](https://cursor.com/help/grok-bot/shared-bots.md#how-do-admins-manage-shared-bots)

## How do I edit or delete a shared Bot?

The owner and the Bot's Managers can change a shared Bot. Click the Bot's name at the top of the chat to open its details, or choose the wrench at the top right to open **Bot settings**:

- **Plugins** (the Bot's connected apps), **Secrets**, **Skills**, and **Files** hold what the Bot uses for everyone.
- Click the name to rename the Bot. Edit the description under **About**.
- **Share** controls who can use the Bot and who manages it.

The owner can also rename the Bot by right-clicking it in the sidebar and choosing **Rename Bot**.

Only the owner can delete a shared Bot. Right-click the Bot in the sidebar and choose **Delete**. A team admin can also delete it from **Manage Bots** in the Cursor dashboard. This deletes the Bot for your whole team. Teammates lose it, along with their chats and routines on it. It can't be undone.

## How do I remove a shared Bot from my sidebar?

Right-click the Bot and choose **Hide from sidebar**. To add it back, choose **+** in the sidebar, then **Browse shared Bots**, and choose **Add** next to it.

If your admin added the Bot to your sidebar for you, **Hide from sidebar** isn't in its menu, and you can't remove it.

## Can I use shared Bots on my phone?

Yes. Shared Bots you've added appear in the phone app. To find another, tap **+**, then **Browse shared Bots**. You can chat with shared Bots and answer their **Allow** cards. A shared Bot can't be your primary Bot.

Sharing and browsing on the phone need Grok Bot 1.19.0 or later on iPhone and Android, from the App Store or Google Play. Earlier versions still open the shared Bots already in your list, and some of their screens still say **Team Bots**.

## Can I voice chat with a teammate's shared Bot?

Yes, on desktop. In your own chat with the Bot, choose **Start voice chat**. See [Voice chat with a Bot](https://cursor.com/help/grok-bot/voice-chat.md).

## Can a shared Bot join a group chat?

Yes. You can add a Bot a teammate shared with you to your own group chat. It can't share a group with Bots that run on your own computer. See [Group chats and Bot-to-Bot messages](https://cursor.com/help/grok-bot/group-chats.md).

## How do admins manage shared Bots?

On the Grok Bot page of the [Cursor dashboard](https://cursor.com/dashboard/bot), open **Manage Bots** under **Shared Bots**.

- **Access** shows who can use each shared Bot. Click it to change who can use the Bot.
- **Auto-add** puts the Bot in members' sidebars automatically. Pick **All team** or one or more groups. Those members can't hide it. Auto-add only applies to groups that have access.
- Admins can also delete a shared Bot here.

Under **Sharing** on the same page:

- **Bot sharing** decides who may share Bots: **Everyone** or **Admins only**. Bots already shared stay shared.
- **Allow Shared Logins** lets Managers share their own app logins as [shared connectors](https://cursor.com/help/grok-bot/shared-bots.md#how-do-shared-connectors-work). Everyone who uses the Bot then acts through that Manager's account. It's off by default.
- **Slack Workspace Access** lets members of your Slack workspace who aren't on the team use Bots shared with your organization. It's on by default, and in an organization it applies to every team. The setting appears as it reaches your team.

See [Grok Bot for Teams and Enterprise](https://cursor.com/docs/grok-bot/teams.md#manage-bots).

## Why can't I see or use a shared Bot?

| What you see                                                                                                 | What it means                                                                                                                                                                                                                                                                                             |
| ------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Browse shared Bots** isn't under **+**                                                                     | You aren't on a Cursor team, or your Grok Bot app needs an update.                                                                                                                                                                                                                                        |
| **Team Bots Not Available**                                                                                  | Your account doesn't have access to shared Bots.                                                                                                                                                                                                                                                          |
| **Only team admins can share Bots**                                                                          | Your team admin limited Bot sharing to admins. **Share** is disabled, and the message appears when you hover it. Ask an admin to share the Bot for you, or to change **Bot sharing** on the team dashboard. See [Who can share Bots?](https://cursor.com/help/grok-bot/shared-bots.md#who-can-share-bots) |
| **Bot Not Found**                                                                                            | The Bot may have been removed, or it isn't shared with you.                                                                                                                                                                                                                                               |
| **No Access to This Bot**                                                                                    | The Bot is shared only with certain people. Ask its owner or a Manager for access.                                                                                                                                                                                                                        |
| A teammate's Bot isn't in **Browse shared Bots**                                                             | The owner hasn't shared it with you yet.                                                                                                                                                                                                                                                                  |
| **Your usage limit has been reached**                                                                        | Your Grok Bot usage ran out. Your chats with a teammate's shared Bot use your usage. See [Plans and billing](https://cursor.com/help/grok-bot/plans.md).                                                                                                                                                  |
| **This Bot's owner has reached their usage limit**                                                           | This reply was billed to the owner's account, and the owner's usage ran out. Ask the owner to check their plan.                                                                                                                                                                                           |
| **This conversation can't run on your computer because your privacy mode is stricter than the bot owner's.** | Your privacy mode setting is stricter than the owner's, so this chat can't use your computer.                                                                                                                                                                                                             |
| In Slack, the Bot asks you to link a Cursor account                                                          | Link your Slack account under **Settings** > **General** > **Team Bots**, using the Cursor account on the Bot's team.                                                                                                                                                                                     |
| In Slack, **some features will be limited**                                                                  | The Bot answered you without a linked account. Link one so it knows who you are and can use your apps.                                                                                                                                                                                                    |
| In Slack, **I haven't been shared with you yet**                                                             | Ask the Bot's owner or a Manager to add you under **Share this Bot**.                                                                                                                                                                                                                                     |
| In Slack, the Bot says it's someone's personal Bot                                                           | Only its owner can talk to it.                                                                                                                                                                                                                                                                            |
| **Your admin has turned off sharing logins with Bots**                                                       | A team admin needs to turn on **Allow Shared Logins** before a Manager can share an account as a shared connector.                                                                                                                                                                                        |

If none of these match, [contact support](https://cursor.com/help/grok-bot/get-help.md) with the Bot's name, the exact message, and your Grok Bot version.

## Related

- [Group chats and Bot-to-Bot messages](https://cursor.com/help/grok-bot/group-chats.md)
- [Connect apps](https://cursor.com/help/grok-bot/connect-apps.md)
- [Store secrets securely](https://cursor.com/help/grok-bot/secrets.md)
- [Plans and billing](https://cursor.com/help/grok-bot/plans.md)
- [Grok Bot for Teams and Enterprise](https://cursor.com/docs/grok-bot/teams.md)


---

## Sitemap

[Overview of all docs pages](/llms.txt)
