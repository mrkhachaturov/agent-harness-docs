# Store secrets securely

Keep passwords, cards, API keys, and other credentials out of chat and ordinary files. Save logins, cards, and contact info in **Vault** so your Bot can sign in and check out for you. Use the secure secret card for API keys. After you save a secret, Grok Bot does not show the value again. A blank field later is not proof the secret was deleted.

## What is Vault?

Vault keeps your logins, cards, and contact info so your Bot can sign in to sites and check out for you without seeing the secret values. Find it in **Settings** > **Vault** on desktop and on the phone. You can add, edit, or remove anything there.

- **Logins**: a website, a username or email, and a password. Your Bot uses a saved login to sign in on that website.
- **Cards**: the number, expiry, security code, name on card, and billing address.
- **Contact info**: names, addresses, phone numbers, and emails for shipping and billing.

Your Bot never sees a saved password, card number, or security code. It can see your contact info and which logins you saved, so it can pick the right entry and type contact details in for you.

Vault isn't supported on [Team Bots](https://cursor.com/help/grok-bot/team-bots.md). For a Team Bot, add keys under **Secrets** instead. See [How should I add an API key or secret?](https://cursor.com/help/grok-bot/secrets.md#how-should-i-add-an-api-key-or-secret)

## How do I add a login, card, or contact info?

1. Open **Settings** > **Vault** and choose **New item**.
2. Pick **Login**, **Card**, or **Contact info**.
3. Fill in the details and save.
   - For a login, enter the **Website**, **Username or email**, and **Password**, then choose **Save login**.
   - For a card, choose **Scan with camera** or **Upload a photo** to fill it from the card, or type it in. Then choose **Save card**.
   - For contact info, enter the name, address, phone, and email, then choose **Save contact info**.

Under **Hints**, tell your Bot when to use an entry, for example "Use for work purchases". Your Bot follows the hint when it picks between entries.

You can also save from a chat:

- When your Bot asks for a login, card, or address with a **Secure Form**, check **Securely save to Bot's vault** to keep it for next time. If you leave it unchecked, the value is kept only for that chat and expires on its own.
- When you attach a photo of a card, Grok Bot offers **Save to Vault** so your Bot can pay with it later.

## How do I import logins from another password manager?

On desktop, you can import logins from a CSV export.

1. Export your passwords as a CSV file from 1Password, Chrome or Edge, Safari or Apple Passwords, Firefox, Bitwarden, or LastPass.
2. In **Settings** > **Vault**, choose **New item**, then **Import from CSV…**.
3. Select **Choose CSV file** and pick the export. The file is read on your computer and never uploaded. It must be under 5 MB.
4. Review the list. Items already in your vault are skipped. Rows with an error, such as a missing password or a website that isn't https, aren't imported.
5. Choose the import button, which shows how many items are ready.

LastPass exports bring cards along too. The exported CSV holds your passwords unencrypted, so delete it once the import finishes.

## How does my Bot use Vault?

- **Signing in**: your Bot uses a saved login first, then a connected password manager such as [1Password](https://cursor.com/help/grok-bot/connect-apps.md#how-do-i-connect-1password). If neither has the login, it asks you with a Secure Form.
- **New accounts**: if you let your Bot pick the password when it signs up for a site, Vault generates the password and saves the login. Your Bot never sees it.
- **Checkout**: saved cards fill in at checkout, and your Bot asks before it uses one. Contact info fills in shipping and billing details.
- **Details you share in chat**: when you give your Bot a name, address, phone number, or email, it saves it as contact info once the task is done and tells you what it saved. Tell it if you don't want something kept.

Your Bot can change contact info, and an entry's nickname and hints, when you ask. Passwords, usernames, websites, card numbers, and security codes change only in **Settings** > **Vault**. Logins and cards are removed only there too.

## How do I change or remove a Vault item?

Open **Settings** > **Vault** and select the item to edit it, or choose **Remove** to delete it. After you remove a login, Grok Bot can no longer sign in to that site with it. After you remove a card, Grok Bot can no longer pay with it.

To change a card's number, remove the card and add it again. On the phone, saved cards can't be edited yet.

## How should I add an API key or secret?

For an API key or other secret that isn't a login or card, use the **secure secret card** when a Bot asks for one. The field is masked. Choose **Save securely**. The card then says **Saved** and **Saved securely and kept private**. The value is not written into the chat.

On a [Team Bot](https://cursor.com/help/grok-bot/team-bots.md) you own or manage, you can also add a secret from the Bot's details. Open **Secrets**, choose **Add secret**, enter an environment variable name, a short description, and the value, then choose **Save secret**. The description is visible to the Bot. The value is not.

Don't paste secrets into chat, Shell, or ordinary files. Don't type them into a demonstration when you use **Teach a task**.

Secrets you save are yours. On a Team Bot you own or manage, secrets are used in every teammate's chat, so only add keys you're happy for everyone who can chat with the Bot to use. A credential your company's setup scripts need, such as a license key for a tool installed on every team computer, is stored by a team admin as a [Team Secret](https://cursor.com/docs/grok-bot/teams.md#team-secrets) on the Enterprise dashboard instead. Those never reach your Bots directly.

## Why can't I see the secret value?

That is expected. Saved values are write-only.

- In **Settings** > **Vault**, saved passwords stay hidden, and cards show only their last four digits.
- The secure secret card does not show the value after **Saved**. The footer says **Stored securely, never shown to your Bot**.
- On a Team Bot, **Secrets** lists the name and description only. It never shows the value again, including in Shell.
- To change a value there, choose **Replace**, paste the new value, and choose **Replace value**. You cannot read the old value back.

If a page asked for the secret, a filled card says **Filled into the page. Secret values were never shown to your Bot.** If it says **Could not fill into the page**, the page may have moved. The value was still not shown to the Bot. Submit a new card if the Bot asks again.

If save fails, the form says **The secret was not saved. Try again.** If a Team Bot's **Secrets** list says **Something went wrong. Try again.**, choose **Try Again**. **No secrets yet** means that Bot has no saved names, not that a value is hidden on the card.

## Did Update delete my secrets?

**Recover**, **Reset**, and computer updates remove installed apps and packages. A secret you typed into a file, a shell profile, or an installed tool on the computer can disappear with that. That is separate from secrets you saved with the secure card, under **Secrets**, or in **Vault**.

Shell not printing a secret does not mean it was wiped. On a Team Bot, if the name is still listed under **Secrets**, the value is still stored. See [Grok Bot computer](https://cursor.com/help/grok-bot/computer-recovery.md) for what Update, Recover, and Reset keep.

If a Team Bot's secret name is gone and you did not choose **Remove**:

1. Fully quit Grok Bot and reopen it. On Mac, choose **Quit** from the menu bar, not just close the window.
2. Open the same Bot on another device signed into the same Cursor account.
3. If the list says **Something went wrong. Try again.**, choose **Try Again** before you add anything.

If the name is still missing on every device, add it again. Don't put it in a file to "keep a copy" on the computer. If names keep disappearing after you did not remove them, [contact support](https://cursor.com/help/grok-bot/get-help.md). Include your account email and a screenshot of **Secrets**. Don't send the secret value.

## Related

- [Connect apps](https://cursor.com/help/grok-bot/connect-apps.md)
- [Grok Bot computer](https://cursor.com/help/grok-bot/computer-recovery.md)
- [Grok Bot How Tos](https://cursor.com/help/grok-bot/how-to.md)
- [Get help](https://cursor.com/help/grok-bot/get-help.md)


---

## Sitemap

[Overview of all docs pages](/llms.txt)
