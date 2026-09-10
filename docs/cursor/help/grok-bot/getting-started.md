# Getting started with Grok Bot

Create agents that take on multi-step work with plugins, a cloud computer, and routines.

## What is Grok Bot?

Grok Bot gives you **agents** you can keep around. An agent can use plugins you've connected, work in a cloud computer, and run routines while you're away. Unlike a one-off chat, an agent can remember context and keep working in the background.

## How do I get started with Grok Bot?

1. Open Grok Bot and [sign in](https://cursor.com/help/grok-bot/sign-in.md) with the **same Cursor account** that should own your plan and usage.
2. Choose one path under [Plans and billing](https://cursor.com/help/grok-bot/plans.md): a Cursor plan that includes Grok Bot, or link SuperGrok, SuperGrok Plus, SuperGrok Heavy, or X Premium+. You can still upgrade within Cursor plans, such as **Pro+** to **Ultra**. Linking SuperGrok on top of a Cursor plan does not add usage.
3. Create your first agent: give it a name, shape, color, and title.
4. In the new chat window, describe the outcome you want and send the message. Suggestions will be presented to help you get started.
5. Send another message anytime to steer or stop the work.
6. If the agent needs a plugin, follow the **Connect** card. See [Connect plugins](https://cursor.com/help/grok-bot/connect-plugins.md).

## What should I know before agents act for me?

Agents can act on real accounts, files, and the web.

For sites without a plugin, the agent can use a browser on the Grok Bot computer. You sign in there yourself; the agent doesn't see your password.

Never paste API keys or other credentials into chat or ordinary files. See [Store secrets securely](https://cursor.com/help/grok-bot/secrets.md).

## How do I organize bots by project or business?

Use **Sidebar Sections** to group bots by project, client, or business without mixing them together.

**On iOS:**

1. Swipe a bot row in the sidebar.
2. Tap **Move to**.
3. Choose **New Section** and name the section for your project or business.
4. Repeat for other bots you want in the same group.

Sections sync between iOS and desktop. Deleting a section moves its bots to **Unassigned** without deleting the bots themselves.

Sidebar Sections require Grok Bot v1.2.0 or later. Update from the App Store if you do not see **Move to**.

## How do I troubleshoot Grok Bot computer, routine, connector, and startup problems?

Most operational issues clear with a full restart. Fully quit Grok Bot (on Mac, choose **Quit** from the menu bar, not just closing the window), reopen, and try again before anything else.

If that doesn't help, match your symptom:

| Symptom                                                                                                                    | What to try                                                                                                                                                                                             | If it persists                                                                                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Computer says **Reconnecting**, **Couldn't Reach Grok Bot's Computer**, **Backup not ready**, or **Bot failed to respond** | Wait and **Retry**, then fully quit and reopen. **Update** if offered. **Recover** if it stays unreachable or the update looks stuck.                                                                   | See [Grok Bot computer](https://cursor.com/help/grok-bot/computer-recovery.md). Use **Reset** only last, and only if you can lose unsynced work.                                        |
| Chats look gone, or bots vanished from the sidebar                                                                         | Fully quit and reopen. Check another device on the same account. Open **Hidden Bots**.                                                                                                                  | See [My chats or bots look missing](https://cursor.com/help/grok-bot/computer-recovery.md#my-chats-or-bots-look-missing-were-they-deleted). Do not **Reset** to look for them.          |
| A secret value is missing in Shell, or secrets look wiped after Update                                                     | A saved value is not shown again. If the name is still listed under **Secrets**, it is still stored.                                                                                                    | See [Store secrets securely](https://cursor.com/help/grok-bot/secrets.md).                                                                                                              |
| A routine isn't running                                                                                                    | Confirm the routine is **Active** and its schedule is correct. See [Routines](https://cursor.com/help/grok-bot/routines.md).                                                                            | If it's **Active** but hasn't run for 24+ hours with no error shown, [report a bug](https://cursor.com/help/troubleshooting/reporting-bugs.md) with the agent name and routine details. |
| An error or crash during a run                                                                                             | Copy the request ID from the message, then try the task again. See [How do I copy a request ID?](https://cursor.com/help/grok-bot/getting-started.md#how-do-i-copy-a-request-id).                       | If the same prompt fails on a fresh run, [report a bug](https://cursor.com/help/troubleshooting/reporting-bugs.md) and include the error text and request ID.                           |
| A plugin won't authorize or shows disconnected                                                                             | Re-add the plugin and finish the provider login in your browser. If it shows **Waiting for authorization**, use **Reopen**. See [Connect plugins](https://cursor.com/help/grok-bot/connect-plugins.md). | If re-authorizing completes but the plugin still shows disconnected, [contact support](https://cursor.com/help/grok-bot/get-help.md) with the plugin name and your account email.       |
| The app hangs on launch                                                                                                    | Fully quit and relaunch. On Mac, use **Quit** from the menu bar.                                                                                                                                        | If it hangs on every launch, [contact support](https://cursor.com/help/grok-bot/get-help.md) with your platform and Grok Bot version.                                                   |

When you contact support or report a bug, include your Cursor account email, your platform and Grok Bot version, the agent name, the exact error text or a screenshot, and the steps you already tried.

## How do I copy a request ID?

Right-click the message and choose **Copy request ID**. You can also hover the message, open **More message actions**, and choose **Copy request ID**.

For a routine, open **Run history**, right-click the run, and choose **Copy request ID**.

Paste the full ID into the report. If **Copy request ID** is not in the menu, that message or run does not have one you can copy. Include the error text and a screenshot instead.

## Why is the Bot asking me to approve something?

An approval card means the Bot stopped and is waiting. The turn does not continue until you choose.

**Auto-review** checks an action before it runs and asks when it needs you. The card may say **The Bot wants to run a command**, **The Bot wants to use a connected service**, **The Bot wants to run a task**, or **Auto-review Paused This Action**.

- **Allow once** lets this action run this time.
- **Always allow** lets this kind of action proceed later and adds a rule under **Auto-review Rules**.
- **Deny** stops this action.

Open **Settings**, then **Bot**, and use the **Auto-review** switch. The description there is **Grok Bot checks each action before it runs and asks you first when needed.** Under **Auto-review Rules**, write one short rule per action. **Ask first** wins if two rules conflict. If the switch says **Required by your admin**, you cannot turn it off.

A secret card, a plugin sign-in, or a page that asks you to type a password is a different prompt. Use the secure card for secrets. See [Store secrets securely](https://cursor.com/help/grok-bot/secrets.md).

## How do I stay up to date?

The desktop app checks for updates automatically. Install a desktop update when the app offers one. Phone updates come from the App Store or Google Play.

Product changes are listed on the [changelog](https://cursor.com/changelog).

## Related

- [Sign in to Grok Bot](https://cursor.com/help/grok-bot/sign-in.md)
- [Plans and billing](https://cursor.com/help/grok-bot/plans.md)
- [Connect plugins](https://cursor.com/help/grok-bot/connect-plugins.md)
- [Routines](https://cursor.com/help/grok-bot/routines.md)
- [Store secrets securely](https://cursor.com/help/grok-bot/secrets.md)
- [Grok Bot on mobile](https://cursor.com/help/grok-bot/mobile.md)
- [Grok Bot computer](https://cursor.com/help/grok-bot/computer-recovery.md)
- [Get help](https://cursor.com/help/grok-bot/get-help.md)


---

## Sitemap

[Overview of all docs pages](/llms.txt)
