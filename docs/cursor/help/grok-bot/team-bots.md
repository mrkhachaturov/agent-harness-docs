# Team Bots

A Team Bot is a Bot one person owns and shares with their Cursor team. The owner chooses who can chat with it: everyone on the team, or only certain people and groups. Each person's chat with a Team Bot is private.

Team Bots always run in the cloud. A Bot that runs on your own computer can't be a Team Bot. Your personal Bots don't change.

## Who can use Team Bots?

Team Bots are for members of a Cursor team who have Grok Bot. To create one, open the command palette with Cmd+K on Mac or Ctrl+K on Windows and Linux, and look for **Create new Team Bot**. If it isn't there, you aren't on a Cursor team, or your Grok Bot app needs an update.

## How do I create a Team Bot?

1. Open the command palette (Cmd+K on Mac or Ctrl+K on Windows and Linux), then choose **Create new Team Bot**. Grok Bot creates a Bot named **New Team Bot** and opens its chat.
2. Tell the Bot what it should help the team with. A sentence is enough.
3. Follow its setup steps. It walks you through apps, secrets, and skills, then files. Only add keys and files you're happy for the whole team to use.
4. Give the Bot a name and description. Click the Bot's name at the top of the chat. Click the name to rename it, and edit the description under **About**. Until you do, its details say **Draft · Only you can see it**, and teammates can't find it.
5. Share it. See [How do I share a Team Bot?](https://cursor.com/help/grok-bot/team-bots.md#how-do-i-share-a-team-bot)

## How do I turn a Bot I already have into a Team Bot?

Click the Bot's name at the top of the chat to open its details. Open **Share** and choose **Share with your Team**. The Bot makes a separate team copy of itself and walks you through what to bring: apps, secrets, skills, memories, and routines, then files.

- Secrets. Only bring keys you're happy for the whole team to use.
- Memories. The Bot shows you which of its memories the team should have. Choose **Share with team** or **Keep private**.
- Routines. You can move them to the team copy or keep them on your personal Bot.

The personal Bot keeps working, and its chats don't move to the team copy. The team copy appears in your sidebar, hidden from teammates until you share it.

The team copy connects to Slack as its own app, with its own handle. Add it to Slack after you share it. See [How do I add a Team Bot to Slack?](https://cursor.com/help/grok-bot/team-bots.md#how-do-i-add-a-team-bot-to-slack)

## How do I share a Team Bot?

When the Bot is ready, it shows a card that says it's ready for your team. Choose **Publish to team** to share it with everyone on your team. After you publish, the card shows **Copy link**, so you can send the Bot to people.

To choose who can use the Bot, click its name at the top of the chat and choose **Share**. In **Share this Bot**:

- Under **Who has access**, choose your team to share the Bot with everyone on the team, or **People you invite** to share it only with the people and groups you add. Limiting it asks you to confirm with **Limit access**. The owner and Managers can always use the Bot.
- Choose **Add people or groups** to add someone. Under **Add as**, pick **Collaborator** to let them chat with the Bot, or **Manager** to let them also change its setup and share it.

Sharing the Bot with anyone else publishes it. **Share** appears once the Bot has a name or a description.

To stop sharing, open the Bot's details and choose **Unpublish**. Only the owner can unpublish. Teammates lose access until you share it again.

## How do teammates find a Team Bot?

- Open the command palette and choose **Team Bots**. The list shows Team Bots shared with you, and each one shows who made it. Choose **Add** to keep a Bot in your sidebar.
- On your phone, open search and tap **Team Bots**.
- Open a link a teammate sent you, then choose **Start a chat**.

To copy a Team Bot's link, right-click it in the sidebar and choose **Copy link**. **Share this Bot** has **Copy link** too. A Team Bot link opens the same shared Bot. It's different from [sharing a Bot template](https://cursor.com/docs/grok-bot/work.md#share-a-bot), which gives each person their own copy.

## Can the owner see my chats with a Team Bot?

No. Each person's chat with a Team Bot is private. The owner and Managers can't read your chats, and you can't read the owner's or anyone else's.

The Bot can save things it learns for the whole team, and it tells you when it does. It doesn't save anything about you personally for the team. What it remembers about working with you stays between you and the Bot.

## Whose apps and secrets does a Team Bot use?

A Team Bot uses the apps and secrets its owner added. Those work the same for everyone who chats with it.

In your own chat with a Team Bot, it can also use your apps. It asks before it uses one of your personal accounts. The card says **Allow**, then the app name:

- **Allow once** lets it use that account this time.
- **Always allow** remembers your answer. Its menu has **Always allow for your messages to this Bot** and **Always allow for your messages to every Team Bot**.
- **Skip** means it doesn't use that account this time.

In Slack channels, threads, and group chats, a Team Bot uses only its owner's apps, and asks before it uses your accounts.

A connected account always acts as the person the Bot is answering. One teammate's connection is never used for someone else.

To make every Team Bot ask again, open **Settings** > **General** > **Team Bots** and choose **Clear** next to **Clear connector preferences**.

## Which computer does a Team Bot use?

In your own chat with a teammate's Team Bot, the Bot usually works on your Grok Bot computer. That means it can use the files there and the sites you're signed in to there. Sometimes it uses a separate computer just for that conversation, for example when your privacy mode is stricter than the owner's.

When you DM a Team Bot in Slack, it also works on your own computer. In Slack channels, threads, group DMs, and group chats, a Team Bot uses one shared computer of its own.

## Whose usage pays for a Team Bot chat?

A Team Bot reply uses the Grok Bot usage of the person it's answering. That's true in your own chat, in Slack, and in group chats. Your own limits apply. The owner's usage pays for the owner's own messages, and for Slack posts from apps or workflows that aren't linked to a Cursor account. See [Plans and billing](https://cursor.com/help/grok-bot/plans.md).

## How do approvals work on a Team Bot?

A Team Bot asks the person it's answering before risky actions.

- In your own chat with a Team Bot, you answer its approval cards.
- In a Slack thread, the Bot posts a **Review an action** card with **Allow once**, **Deny**, and **View details**. Only the person who asked can answer it.
- In a group chat, only the person whose message the Bot is answering can answer.

It also asks before it uses your personal accounts. See [Whose apps and secrets does a Team Bot use?](https://cursor.com/help/grok-bot/team-bots.md#whose-apps-and-secrets-does-a-team-bot-use)

## How do I add a Team Bot to Slack?

The owner or a Manager adds it, after sharing:

1. Click the Bot's name at the top of the chat.
2. Find **Bring to your team's Slack** and choose **Connect**. Before the Bot is published, the row says **Slack** and **Connect after publishing**.
3. If it says **Awaiting admin approval**, a Slack workspace admin needs to approve the app.

Once it says **Connected**, teammates can message the Bot directly or mention it in channels.

In a channel thread or a DM, the Team Bot acts for the teammate who mentioned it. It can hand work to that person's own Bots, and their replies are posted back into the same thread. A personal Bot doesn't hand work to other Bots from a channel thread. See [Can a Bot message other Bots from Slack?](https://cursor.com/help/grok-bot/group-chats.md#can-a-bot-message-other-bots-from-slack)

Bots record who asked for each message they post in Slack, so anyone in the thread can ask the Bot who requested it. When a Team Bot's routine replies in a Slack thread, the Bot follows that thread and answers later replies without an @mention.

Each teammate needs to link their Slack account first. Open **Settings** > **General** > **Team Bots** and choose **Link**. If you message the Bot before you link, it replies with steps to link your account.

## How do I edit, unpublish, or delete a Team Bot?

The owner and the Bot's Managers can change a Team Bot. Click the Bot's name at the top of the chat to open its details:

- **Plugins** (the Bot's connected apps), **Secrets**, **Skills**, and **Files** hold what the Bot uses for everyone.
- Click the name to rename the Bot. Edit the description under **About**.
- **Share** controls who can use the Bot and who manages it.

Only the owner can unpublish or delete a Team Bot. **Unpublish** is in the Bot's details, and hides the Bot from teammates until you share it again.

The owner can also rename the Bot by right-clicking it in the sidebar and choosing **Rename Bot**.

To delete it, right-click the Bot in the sidebar and choose **Delete**. This deletes the Bot for your whole team. Teammates lose it, along with their chats and routines on it. It can't be undone.

## How do I remove a Team Bot from my sidebar?

Right-click the Bot and choose **Hide from sidebar**. To add it back, open the command palette, choose **Team Bots**, and choose **Add** next to it.

If your admin added the Bot to your sidebar for you, **Hide from sidebar** isn't in its menu, and you can't remove it.

## Can I use Team Bots on my phone?

Yes, for chatting. Team Bots you've added appear in the phone app. To find another, open search and tap **Team Bots**. You can chat with Team Bots and answer their **Allow** cards. A Team Bot can't be your primary Bot.

Create, share, edit, and connect Team Bots to Slack on desktop.

## Can I voice chat with a teammate's Team Bot?

Yes, on desktop. In your own chat with the Bot, choose **Start voice chat**. See [Voice chat with a Bot](https://cursor.com/help/grok-bot/voice-chat.md).

## Can a Team Bot join a group chat?

Yes. You can add a teammate's published Team Bot to your own group chat. It can't share a group with Bots that run on your own computer. See [Group chats and Bot-to-Bot messages](https://cursor.com/help/grok-bot/group-chats.md).

## How do admins manage Team Bots?

On the Grok Bot page of the [Cursor dashboard](https://cursor.com/dashboard/bot), open **Manage Team Bots** under **Team Bots**.

- **Access** shows who can use each Team Bot. Click it to change who can use the Bot.
- **Auto-add** puts the Bot in members' sidebars automatically. Pick **All team** or one or more groups. Those members can't hide it. Auto-add only applies to groups that have access.

See [Grok Bot for Teams and Enterprise](https://cursor.com/docs/grok-bot/teams.md#manage-team-bots).

## Why can't I see or use a Team Bot?

| What you see                                                                                                 | What it means                                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Create new Team Bot** isn't in the command palette                                                         | You aren't on a Cursor team, or your Grok Bot app needs an update.                                                                                     |
| **Team Bots Not Available**                                                                                  | Your account doesn't have access to Team Bots.                                                                                                         |
| **Bot Not Found**                                                                                            | The Bot may have been removed, or it isn't shared with you.                                                                                            |
| **No Access to This Bot**                                                                                    | The Bot is shared only with certain people. Ask its owner or a Manager for access.                                                                     |
| A teammate's Bot isn't in **Team Bots**                                                                      | The owner hasn't shared it yet, it isn't shared with you, or it still has the default name and no description.                                         |
| **Your usage limit has been reached**                                                                        | Your Grok Bot usage ran out. Your chats with a teammate's Team Bot use your usage. See [Plans and billing](https://cursor.com/help/grok-bot/plans.md). |
| **This Bot's owner has reached their usage limit**                                                           | This reply was billed to the owner's account, and the owner's usage ran out. Ask the owner to check their plan.                                        |
| **This conversation can't run on your computer because your privacy mode is stricter than the bot owner's.** | Your privacy mode setting is stricter than the owner's, so this chat can't use your computer.                                                          |
| In Slack, the Bot asks you to link a Cursor account                                                          | Link your Slack account under **Settings** > **General** > **Team Bots**, using the Cursor account on the Bot's team.                                  |

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
