# Connect apps

Connect Gmail, Notion, Slack, and other apps so your Bots can use them in chat.

## What are apps?

Apps let your Bots work with external services. App connections belong to the **same account** you used to sign in to Grok Bot.

The **Email** app is different: it gives your Bots their own email address instead of connecting an account you already have. See [Give your Bot an email address](https://cursor.com/help/grok-bot/agent-email.md).

## How do I add an app?

1. In Grok Bot, select **Connect apps** in the sidebar, or follow an in-chat **Connect** card. In the Grok Bot mobile app, tap your avatar on the top left and select **Connect apps**.
2. Browse or search for the app, then add it.
3. When Grok Bot asks you to **Authorize** or **Authenticate**, finish the provider login in your browser.
4. If sign-in doesn't finish, choose **Reconnect** on the app, or **Reopen** on the in-chat card, to bring the sign-in page back.
5. Confirm the app appears under **Installed**.

## Why does an app say "Disabled by team admin"?

If you use Grok Bot through a Cursor team, your Cursor team admin controls which apps are available. If an app is disabled, ask your admin to enable it.

That Cursor control is separate from a company Google admin. A Google block uses the screens in the next section.

## What if Google says an admin needs to review Grok?

A company Google account can stop the connection before Gmail, Calendar, Drive, Docs, Sheets, or Slides finishes signing in. Grok Bot signs in to Google as **Grok**, not Cursor. The Google page decides the next step.

**Your admin needs to review Grok**

Grok is not approved for that Workspace yet. On the Google page, request access if that button is there. Wait for the admin to approve Grok before you try **Authorize** again.

An IT admin approves **Grok** in the Google Admin console:

1. Open **Security**, then **Access and data control**, then **API controls**.
2. Open **App access control**, then **Manage third-party app access**.
3. Add the app named **Grok**. If name search does not find it, use the client ID from the blocked page or the admin review email.
4. Set Grok to **Trusted** for the people who use Grok Bot.

That approval covers the Google apps those people connect. It does not turn an app back on in Cursor. A Cursor team admin does that from the **Disabled by team admin** control above.

**Access blocked**

Google refused the sign-in. A personal Gmail account does not need a company admin. A company account often hits this when Grok is not on the allowlist, or when the admin has blocked third-party apps.

Ask the Google admin to trust **Grok**, using the steps above. If the page still says access is blocked after that, [contact support](https://cursor.com/help/grok-bot/get-help.md) with the Google account email and a screenshot of the blocked page. Changing browsers or connecting the app again does not clear a Google admin block.

## What can a connected app do?

An app uses the account you authorize. It can do only what that account can already do in that service. It cannot raise your access, and it cannot change sharing.

**Google Calendar**

The bot can read calendars you can see, create and update events, check free time, and respond to invitations on calendars you can edit.

It cannot change Google Meet settings, such as the waiting room or host controls. It also cannot add a Zoom link to an event. A Zoom link added from the Calendar website uses Google's Zoom add-on, and that add-on is not available to the app. Put the Zoom link in the event location or description yourself, or create the event in Calendar and ask the bot to update the other fields.

**Google Sheets**

Connecting Sheets lets the bot read and edit cells in spreadsheets the connected Google account can edit. A file shared as Viewer stays view-only. The app cannot change who has access.

Finding and opening files uses the **Google Drive** app. Drive can search and read files that account can open. Editing cell content uses **Google Sheets**.

**Slack**

The Slack app posts as the Slack user you connected, not as a separate bot that has to be invited. It can post only in channels that user can post in. It cannot post in a private channel that user is not in, or in a channel where that workspace blocks posting. To use another Slack workspace, connect that workspace. This is separate from a Slack message that starts a routine. See [Routines](https://cursor.com/help/grok-bot/routines.md#how-do-slack-triggers-work).

**Gmail**

Gmail can search and read mail, draft and send, and apply labels on the connected mailbox.

## Can I connect two Gmail accounts?

No. Gmail connects one mailbox at a time. To use a different Gmail mailbox, disconnect the current one and authorize the other. You cannot keep a personal mailbox and a work mailbox connected to Gmail at the same time.

A connected app is available to every bot on that Grok Bot account. Disconnect Gmail if a bot should not use that mailbox. A teammate's [Team Bot](https://cursor.com/help/grok-bot/team-bots.md) asks before it uses your accounts.

Some other apps, like Notion, can connect a second account. See [How do I add a second account for the same app?](https://cursor.com/help/grok-bot/how-to.md#how-do-i-add-a-second-account-for-the-same-app)

## An app is added, but the Bot says it's missing. What do I do?

**Added** means the app is installed, not that you are signed in. Open the app and choose **Authenticate** (**Authorize** on the phone) if it shows **Needs auth** or **Disconnected**. For a connect card that never shows up or does nothing, see [How do I reconnect an app?](https://cursor.com/help/grok-bot/how-to.md#how-do-i-reconnect-an-app)

## Why does connecting to Zoom fail with error 4700 during authorization?

This is a known issue, and our engineers are working on a fix. Zoom authorization from the Grok Bot desktop app currently fails with error 4700 (Invalid redirect), and no change on your end will resolve it.

There is no workaround for now. We will update this article once Zoom can be connected.

## Why does SharePoint admin consent fail with a redirect URI error (AADSTS50011)?

This is a known issue, and our engineers are working on a fix. When a Cursor team admin connects SharePoint from the dashboard **Integrations** page and chooses **Application-level permissions**, Microsoft shows AADSTS50011 (redirect URI mismatch) before the consent prompt. The Microsoft app named in the error belongs to Grok, not your organization, so nothing in your tenant causes this and no change in your Entra admin center will clear it.

Workaround: connect with **Delegated permissions** instead.

1. In the Cursor dashboard, open **Integrations** and find the SharePoint card.
2. Choose **Connect team** (or **Reconnect** if you already started setup) and pick **Delegated permissions**.
3. Enter your Microsoft tenant ID (for example contoso.onmicrosoft.com, or the GUID from Microsoft Entra ID > Overview).
4. Sign in with Microsoft. Most work or school tenants need a Microsoft admin to consent once to Sites.Read.All.
5. Each team member signs in with their own Microsoft account the first time a bot uses SharePoint. They see only the sites their account can already open.

If you started Application-level setup and members now see "This team does not have the SharePoint integration", the admin needs to finish the Delegated sign-in above. The app stays unavailable until that Microsoft step completes.

We will update this article when Application-level permissions can be approved.

## Related

- [Store secrets securely](https://cursor.com/help/grok-bot/secrets.md)
- [Sign in to Grok Bot](https://cursor.com/help/grok-bot/sign-in.md)
- [Grok Bot How Tos](https://cursor.com/help/grok-bot/how-to.md)
- [Get help](https://cursor.com/help/grok-bot/get-help.md)


---

## Sitemap

[Overview of all docs pages](/llms.txt)
