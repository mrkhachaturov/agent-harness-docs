# Grok Bot computer

The Grok Bot computer is shared by your bots. Files, logins, installed apps, and the browser live there. Chats are stored separately, so a computer problem does not delete conversation history by itself.

Open computer controls from **Settings > Updates**. You can also get **Recover** from the reconnect screen when the app offers it.

## What do Update, Recover, and Reset each do?

| Action      | What it does                                                                                                     | What it keeps                                    | What it removes                                                              |
| ----------- | ---------------------------------------------------------------------------------------------------------------- | ------------------------------------------------ | ---------------------------------------------------------------------------- |
| **Update**  | Moves the computer to the latest version. You can update now or schedule it for later.                           | Bots, files, and logins that have already synced | Installed apps and packages. A turn that cannot pause is discarded.          |
| **Recover** | Recreates the computer and reconnects.                                                                           | Bots, files, and logins                          | Installed apps and packages                                                  |
| **Reset**   | Restores the last saved snapshot and starts a fresh computer on the latest version. Running work is interrupted. | Only what is already in that snapshot            | Recent bots and files that have not synced yet. Installed apps and packages. |

**Reset** is the only one that can drop recent bots and files. If bots recently disappeared, or saving failed, cancel **Reset** and [contact support](https://cursor.com/help/grok-bot/get-help.md).

## Which should I try first?

1. Wait, then choose **Retry** if the computer says **Reconnecting** or **Couldn't Reach Grok Bot's Computer**. Bots, files, and logins are safe while it reconnects. Do not **Reset** during this.
2. Fully quit Grok Bot and reopen it. On Mac, choose **Quit** from the menu bar, not just close the window.
3. **Update** the computer from **Settings > Updates** if an update is offered.
4. **Recover** if it still cannot reconnect, or if an update looks stuck and **Recover computer** is shown. On a slow update, **Keep waiting** is the safe default.
5. **Reset** only after those steps, and only if you can lose unsynced work.

Do not start a second Update or Reset while one is already running. Repeated resets can interrupt a restore that is still finishing.

## How long should I wait?

- **Reconnecting** and **Recover** usually take a few minutes. You can choose **Continue in Background**.
- An **Update** can also take a few minutes when it is downloading a large image or transferring data. If it says **Update still running**, keep waiting.
- Choose **Recover** only if the update appears stuck and the app offers **Recover computer**. If recovery is not available, keep waiting.
- If **Recover** or **Reset** fails, use **Retry Recovery** or **Retry Reset** once. Then stop and [contact support](https://cursor.com/help/grok-bot/get-help.md).

## Why does Update say Backup not ready?

The computer's data is not safely backed up yet. Grok Bot will offer the update again after a backup completes. Wait for that. Do not **Reset** to force the update.

**Agent busy** means a bot could not pause in time, so the computer was not updated. Let that bot finish, then update again.

## Why did a bot fail to respond?

Check the computer first. A bot cannot finish a turn while the computer says **Reconnecting** or **Couldn't Reach Grok Bot's Computer**. Follow [Which should I try first?](https://cursor.com/help/grok-bot/computer-recovery.md#which-should-i-try-first), then send the message again.

If the computer is connected and the same prompt still fails, [contact support](https://cursor.com/help/grok-bot/get-help.md). Include the error title, such as **Bot failed to respond**, and a screenshot of the computer status.

## What happens if I delete files inside the computer?

Conversation history is stored outside the computer, so deleting files inside it, including `rm -rf`, does not delete chats.

Grok Bot keeps a durable copy of synced computer data. Reopening the computer restores from that copy, so synced files usually come back. If the computer is still empty after **Recover**, stop making changes inside it and [contact support](https://cursor.com/help/grok-bot/get-help.md).

Files that exist only on your Mac or Windows machine are not covered. Keep your own backups for those.

| Data type                            | Recoverable?                                                                          |
| ------------------------------------ | ------------------------------------------------------------------------------------- |
| Agent conversation history           | Yes. Stored outside the computer.                                                     |
| Computer files already synced        | Yes. Restored when the computer reopens, or from the last snapshot on **Reset**.      |
| Recent bots and files not yet synced | No, if you **Reset**. **Recover** and **Update** keep synced bots, files, and logins. |
| Installed apps and packages          | No. **Update**, **Recover**, and **Reset** all remove them.                           |
| Files on your Mac or Windows machine | No. Use your own backups.                                                             |

## My chats or bots look missing. Were they deleted?

Often no. Chats are stored separately from the computer, so a computer problem does not delete conversation history by itself. Check before you **Reset**.

1. Fully quit Grok Bot and reopen it. On Mac, choose **Quit** from the menu bar, not just close the window.
2. Open the same account on another device, including the iPhone app. Bots and conversations are shared across devices signed into that account.
3. In the sidebar, open **Hidden Bots** or **Show Hidden Bots**. **Hide from sidebar** removes a Bot from the list only. Hidden Bots stay active and keep their history. Choose **Unhide** to show one again.
4. Confirm you are in the same Cursor account, not a different login.

A disk warning is not data loss. **Computer is low on disk space** or **Computer is critically low on disk space** means Disk Saver is auditing usage and will propose safe cleanup. Nothing is deleted without confirmation. **Disk Saver** is a Bot in the sidebar. Choose **Go to Disk Saver** to review what it proposes. Declining leaves those files in place. Cleanup applies only to computer files you confirm, not to chats.

**Reset** is different. It can drop recent bots and files that have not synced. Don't **Reset** to look for chats that seem missing. If they are still missing on every device after the checks above, [contact support](https://cursor.com/help/grok-bot/get-help.md). Include your account email, the Bot name, and a screenshot of the sidebar.

## When should I contact support?

Contact support instead of trying another **Reset** if:

- Bots or chats still look missing on every device after the checks in [My chats or bots look missing](https://cursor.com/help/grok-bot/computer-recovery.md#my-chats-or-bots-look-missing-were-they-deleted), or saving failed
- **Backup not ready** does not clear
- **Recover** or **Reset** fails after one retry
- The computer is still empty after **Recover**

Include your Cursor account email, Grok Bot version, which action you already tried, the agent name, and a screenshot of the computer status.

## Related

- [Grok Bot How Tos](https://cursor.com/help/grok-bot/how-to.md)
- [Grok Bot on mobile](https://cursor.com/help/grok-bot/mobile.md)
- [Store secrets securely](https://cursor.com/help/grok-bot/secrets.md)
- [Get help](https://cursor.com/help/grok-bot/get-help.md)


---

## Sitemap

[Overview of all docs pages](/llms.txt)
