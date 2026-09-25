# Grok Bot How Tos

Short answers for organizing bots, updating the app, fixing plugins, signing in to work apps, approvals, notifications, and the problems that usually clear without a reset. First-time setup is on [Onboarding](https://cursor.com/help/grok-bot/onboarding.md).

## How do I organize bots by project or business?

Use **Sidebar Sections** to group bots by project, client, or business without mixing them together.

**On iOS:**

1. Swipe a bot row in the sidebar.
2. Tap **Move to**.
3. Choose **New Section** and name the section for your project or business.
4. Repeat for other bots you want in the same group.

Sections sync between iOS and desktop. Deleting a section moves its bots to **Unassigned** without deleting the bots themselves.

Sidebar Sections require Grok Bot v1.2.0 or later. Update from the App Store if you do not see **Move to**.

## How do I hide a Bot from the sidebar?

Choose **Hide from sidebar**. The Bot stays active and keeps its history. A hidden Bot doesn't send notifications.

To show it again on desktop, open **Hidden Bots**, right-click the Bot, and choose **Show in sidebar**. On the phone, open **Show Hidden Bots** and choose **Unhide**.

If it is missing from both lists, use the checks in [My chats or bots look missing](https://cursor.com/help/grok-bot/computer-recovery.md#my-chats-or-bots-look-missing-were-they-deleted).

## How do I troubleshoot Grok Bot computer, routine, connector, and startup problems?

Most operational issues clear with a full restart. Fully quit Grok Bot (on Mac, choose **Quit** from the menu bar, not just closing the window), reopen, and try again before anything else.

If that doesn't help, match your symptom:

| Symptom                                                                                                                    | What to try                                                                                                                                                                                                                            | If it persists                                                                                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Computer says **Reconnecting**, **Couldn't Reach Grok Bot's Computer**, **Backup not ready**, or **Bot failed to respond** | Wait and **Retry**, then fully quit and reopen. **Update** if offered. **Recover** if it stays unreachable or the update looks stuck.                                                                                                  | See [Grok Bot computer](https://cursor.com/help/grok-bot/computer-recovery.md). Use **Reset** only last, and only if you can lose unsynced work.                                        |
| Chats look gone, or bots vanished from the sidebar                                                                         | Fully quit and reopen. Check another device on the same account. Open **Hidden Bots**.                                                                                                                                                 | See [My chats or bots look missing](https://cursor.com/help/grok-bot/computer-recovery.md#my-chats-or-bots-look-missing-were-they-deleted). Do not **Reset** to look for them.          |
| A secret value is missing in Shell, or secrets look wiped after Update                                                     | A saved value is not shown again. If the name is still listed under **Secrets**, it is still stored.                                                                                                                                   | See [Store secrets securely](https://cursor.com/help/grok-bot/secrets.md).                                                                                                              |
| A routine isn't running                                                                                                    | Confirm the routine is **Active** and its schedule is correct. See [Routines](https://cursor.com/help/grok-bot/routines.md).                                                                                                           | If it's **Active** but hasn't run for 24+ hours with no error shown, [report a bug](https://cursor.com/help/troubleshooting/reporting-bugs.md) with the agent name and routine details. |
| An error or crash during a run                                                                                             | Copy the request ID from the message, then try the task again. See [How do I copy a request ID?](https://cursor.com/help/grok-bot/how-to.md#how-do-i-copy-a-request-id).                                                               | If the same prompt fails on a fresh run, [report a bug](https://cursor.com/help/troubleshooting/reporting-bugs.md) and include the error text and request ID.                           |
| A plugin won't authorize or shows disconnected                                                                             | Re-add the plugin and finish the provider login in your browser. If it shows **Waiting for authorization**, use **Reopen**. See [How do I reconnect a plugin?](https://cursor.com/help/grok-bot/how-to.md#how-do-i-reconnect-a-plugin) | If re-authorizing completes but the plugin still shows disconnected, [contact support](https://cursor.com/help/grok-bot/get-help.md) with the plugin name and your account email.       |
| The app hangs on launch                                                                                                    | Fully quit and relaunch. On Mac, use **Quit** from the menu bar.                                                                                                                                                                       | If it hangs on every launch, [contact support](https://cursor.com/help/grok-bot/get-help.md) with your platform and Grok Bot version.                                                   |

When you contact support or report a bug, include your Cursor account email, your platform and Grok Bot version, the agent name, the exact error text or a screenshot, and the steps you already tried. Copy the version from [About](https://cursor.com/help/grok-bot/how-to.md#how-do-i-find-my-grok-bot-version).

## How do I copy a request ID?

Right-click the message and choose **Copy request ID**. You can also hover the message, open **More message actions**, and choose **Copy request ID**.

For a routine, open **Run history**, right-click the run, and choose **Copy request ID**.

Paste the full ID into the report. If **Copy request ID** is not in the menu, that message or run does not have one you can copy. Include the error text and a screenshot instead.

## How do I find my Grok Bot version?

Open the account menu and choose **About**. The dialog shows **Version**, and **Copy version info** copies the version, release track, and OS. That is the version to send with a support request.

## How do I update Grok Bot?

The desktop app checks for updates on its own. When one is ready, the account menu shows **New update available**. Choose **Install**, then **Restart to update**. Your Bots keep working in the cloud while the app restarts.

To check yourself, open **Settings**, go to **Updates**, and choose **Check for Updates**. If an update is ready, choose **Restart to Update**. **Automatic Updates** installs updates while you're away.

Phone updates come from the App Store or Google Play. Product changes are listed on the [changelog](https://cursor.com/changelog).

## Why does Grok Bot say Update required?

Grok Bot requires an update when your version is more than 14 days old and a newer version is out. The app shows **Update required** and says your version is no longer supported.

1. Choose **Update**.
2. When the download finishes, choose **Restart to update**.
3. If the update fails, choose **Try again**. You can also choose **Download the latest version** and install it yourself.

On Linux, the screen may show a command to run instead. Choose **Copy command**, run it in a terminal, then restart Grok Bot. The command depends on how you installed Grok Bot:

- Debian or Ubuntu: `sudo apt update && sudo apt install --only-upgrade grok-bot`
- Fedora or other RPM systems: `sudo dnf upgrade --refresh grok-bot`

If the screen asks you to download and install the latest package, do that, then restart Grok Bot.

On the phone, **Update required** has an **Update Grok Bot** button that opens the App Store or Google Play.

## Grok Bot closed to update, but it is still on the old version. What do I do?

1. Check the version. Open the account menu and choose **About**.
2. Fully quit Grok Bot and reopen it. On Mac, choose **Quit** from the menu bar, not just close the window.
3. Open **Settings**, go to **Updates**, and choose **Check for Updates**. Then choose **Restart to Update**.
4. If the version still hasn't changed, download the latest version from [cursor.com/dashboard/bot](https://cursor.com/dashboard/bot) and install it over the current app. Your Bots and chats belong to your account, so they are still there after you reinstall.
5. On Linux, run the update command for your system. See [Why does Grok Bot say Update required?](https://cursor.com/help/grok-bot/how-to.md#why-does-grok-bot-say-update-required)

If the old version keeps coming back, [contact support](https://cursor.com/help/grok-bot/get-help.md) with the version from **About** and your platform.

## How do I change the app language?

On desktop, open **Settings**, go to **General**, and choose a **Language** under **Appearance**. **Follow System** uses your computer's language. Desktop has 31 languages: English, Afrikaans, Arabic, Bengali, Chinese (Simplified), Chinese (Traditional), Czech, Danish, Dutch, Finnish, French, German, Greek, Hebrew, Hindi, Hungarian, Indonesian, Italian, Japanese, Korean, Norwegian Bokmål, Polish, Portuguese, Russian, Spanish, Swedish, Thai, Turkish, Ukrainian, Urdu, and Vietnamese.

On the phone, open **Settings** and choose **Language**. **System** uses your phone's language. The phone app has English, Chinese (Simplified), Chinese (Traditional), French, German, Hindi, Japanese, Korean, Polish, Portuguese, and Spanish.

The language changes the app's menus and messages. New Bots write to you in that language unless you write to them in another one. Voice chat has its own **Language** setting. See [Voice chat with a Bot](https://cursor.com/help/grok-bot/voice-chat.md).

## How do I reconnect a plugin?

Match what you see:

**The connect card never shows up.** A Bot shows a connect card only when a plugin needs you to sign in. Don't wait for one. Open **Plugins** in the sidebar, open the plugin, and choose **Authorize**.

**The connect card does nothing, or sign-in didn't finish.** If the card says it is waiting for authorization, choose **Reopen** to bring the sign-in page back. If it says authorization didn't finish or failed, choose **Retry**. Finish the sign-in in your browser within about 10 minutes, or start again from the card.

**The plugin says Added, but the Bot says it's missing.** **Added** means the plugin is installed. It doesn't mean you are signed in. Open **Plugins**, open the plugin, and check its status:

- **Needs auth** or **Disconnected**: choose **Authorize** and finish the sign-in.
- **Disabled by team admin**: ask your Cursor team admin to turn it on. See [Why does a plugin say "Disabled by team admin"?](https://cursor.com/help/grok-bot/connect-plugins.md#why-does-a-plugin-say-disabled-by-team-admin)
- **Connected**: send the Bot a new message and ask it to try the plugin again.

If it still doesn't work, choose **Remove**, add the plugin again, and sign in. If that doesn't help, [contact support](https://cursor.com/help/grok-bot/get-help.md) with the plugin name and your account email.

## How do I add a second account for the same plugin?

Some plugins can connect more than one account, like two Notion workspaces.

1. Open **Plugins** in the sidebar and open the plugin.
2. Under **Accounts**, choose **Add Another Account**.
3. Give the account a label, like work or personal.
4. Choose **Authorize** and sign in to the second account.

On the phone, choose **Authorize new account**.

Tell the Bot which account to use by its label. For example: "Use my work Notion." Every Bot on your Grok Bot account can use every connected account.

If you don't see **Add Another Account**, that plugin connects one account at a time. See [Can I connect two Gmail accounts?](https://cursor.com/help/grok-bot/connect-plugins.md#can-i-connect-two-gmail-accounts)

## How do I sign in to a work app that uses Okta or single sign-on?

Your Bots work on their own cloud computer, not on your laptop. Fingerprint, Face ID, Windows Hello, and passkeys saved on your laptop or phone don't work on the Bot's computer. You sign in there yourself.

1. Ask the Bot to open the work app.
2. When it reaches the sign-in page, the Bot shows a **Computer** card marked **Action needed**.
3. Choose **Take over**. You now control the Bot's computer.
4. Sign in with a method your company allows there, such as a password with a code or a push approval on your phone.
5. Choose **I'm done**. The Bot continues.

Choose **Skip** if you don't want to sign in now.

On Mac and Windows, you can also use a hardware security key, such as a YubiKey, plugged into your computer. Open **Settings**, go to **General**, and under **Security Key** turn on **Use hardware security keys**. Grok Bot asks you to approve each use.

All your Bots share one computer. After you sign in, every Bot on your account can use that sign-in until it expires. Don't sign in to an account on the Bot's computer if one of your Bots shouldn't use it.

## Why is the Bot asking me to approve something?

An approval card means the Bot stopped and is waiting. The action does not run until you choose.

**Auto-review** checks an action before it runs and asks when it needs you. The card says **Review an action**.

- **Allow once** lets this action run this time.
- **Always allow** lets this kind of action run later without asking. It adds a rule under **Auto-review Rules**.
- **Deny** stops this action.

Open **Settings**, then **Bot**, and use the **Auto-review** switch. The description there is **Grok Bot checks each action before it runs and asks you first when needed.** Under **Auto-review Rules**, write one short rule per action. **Ask first** wins if two rules conflict. If the switch says **Required by your admin**, you cannot turn it off.

A secret card, a plugin sign-in, or a page that asks you to type a password is a different prompt. Use the secure card for secrets. See [Store secrets securely](https://cursor.com/help/grok-bot/secrets.md).

## Where do pending approvals show up?

- **In the chat.** The approval card is in that Bot's chat.
- **In the sidebar.** The Bot shows that it needs attention.
- **As a notification.** If the Bot's **Notifications** switch is on, you get an alert that the Bot needs you. Desktop alerts don't show while Grok Bot is the window you're using. The sidebar still shows them.

On the phone, allow notifications for Grok Bot in your phone settings to get alerts there. See [How do I stop phone notifications while I work on desktop?](https://cursor.com/help/grok-bot/mobile.md#how-do-i-stop-phone-notifications-while-i-work-on-desktop)

## Why did an approval expire?

An approval from a chat you are in waits for you. An approval from work that started without you, like a routine, a trigger, or a message from another Bot, expires after about 10 minutes. The card then shows **Expired**, and the action doesn't run.

To catch approvals in time:

- Turn on **Notifications** for Bots that run routines. The switch is in the Bot's **Bot settings** on desktop and in its profile on the phone.
- Choose **Always allow** for actions you trust, so the Bot doesn't need to ask next time. An expired card may offer **Always allow this in the future**.
- Ask the Bot to try the task again after an approval expires.

## How do I turn off notifications for helper Bots?

A helper Bot is a Bot that one of your Bots created to help with its work. It shows up in your sidebar and notifies you like any other Bot.

On desktop, open the helper Bot's chat, click its name at the top, and choose **Bot settings**. Turn off **Notifications**. The note there is **Get notified when this Bot finishes or needs input**.

On the phone, open the helper Bot's chat, tap its name at the top, and turn off **Notifications**.

You can also hide the helper Bot. A hidden Bot doesn't send notifications. See [How do I hide a Bot from the sidebar?](https://cursor.com/help/grok-bot/how-to.md#how-do-i-hide-a-bot-from-the-sidebar)

## Related

- [Onboarding](https://cursor.com/help/grok-bot/onboarding.md)
- [Grok Bot FAQs](https://cursor.com/help/grok-bot/faqs.md)
- [Change a Bot's name, picture, and description](https://cursor.com/help/grok-bot/edit-bot.md)
- [Group chats and Bot-to-Bot messages](https://cursor.com/help/grok-bot/group-chats.md)
- [Voice chat with a Bot](https://cursor.com/help/grok-bot/voice-chat.md)
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
