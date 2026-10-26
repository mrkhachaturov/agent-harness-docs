# Minimum version policy

Older Cursor versions show an update warning and later stop working until you update. Here's how the policy works, how you'll be warned, and how to update.

## What is Cursor's minimum version policy?

Cursor keeps two minimum versions:

- **Minimum supported version**: older versions keep working but show a "please update" warning. A release usually reaches this point about 2 months after it ships.
- **Minimum allowed version**: older versions stop working. Agent requests fail with an "Update Required" error until you update. A release usually reaches this point about 3 months after it ships.

## Why does Cursor have a minimum version policy?

Keeping everyone on a recent version means reliability fixes, security updates, and new features reach every user.

## What is the current minimum version schedule?

Current schedule as of October 26, 2026. These dates may change.

| Date         | Change                                                                 | What it means for users                                                                 |
| ------------ | ---------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| Oct 26, 2026 | Minimum allowed version is now 3.6. Minimum supported version is 3.18. | Versions older than 3.6 stop working. Versions older than 3.18 show the update warning. |
| Nov 22, 2026 | Minimum allowed version becomes 3.12                                   | Versions older than 3.12 stop working                                                   |
| Dec 14, 2026 | Minimum allowed version becomes 3.18                                   | Versions older than 3.18 stop working                                                   |

## How will I know my Cursor version is about to stop working?

Cursor shows an "Update recommended" message shortly after the editor opens, and an "Update Available" notice below the response after agent requests. The message says when your version stops working, for example "This version of Cursor stops working on November 22, 2026." Each message has an **Update** button.

- If you're on a team, the message also asks you to contact your IT admin
- Enterprise accounts with many users on an affected version hear from their account team ahead of time

## What happens when my Cursor version reaches the minimum allowed version?

Cursor still opens, but it shows an "Update required" message and agent requests fail with an "Update Required" error until you update. Nothing is deleted: your chat history and settings are still there after you update.

## Does Cursor update automatically?

Most of the time, yes. Cursor either updates itself or prompts you to update. Updates don't happen automatically when:

- The `update.mode` setting on your machine is set to `none` (updates are off) or `manual` (Cursor only updates when you check). To check it, switch to the editor, open the Command Palette with **Cmd/Ctrl+Shift+P**, run **Preferences: Open Settings (UI)**, and search for `update.mode`.
- Your admin set the `UpdateMode` MDM policy. The policy overrides your own `update.mode` setting.

In those cases, update manually using the steps below, or ask your admin to deploy the latest version. See the [UpdateMode policy](https://cursor.com/docs/enterprise/deployment-patterns.md#updatemode-policy) in the [MDM configuration](https://cursor.com/docs/enterprise/deployment-patterns.md#mdm-configuration) docs for every available value.

## How do I update Cursor to a supported version?

1. Download the latest version from [cursor.com/download](https://cursor.com/download)
2. Install it over your current version. Your settings and chat history carry over.

You can also update from inside the app: click **Update** in the update message, or press **Cmd/Ctrl+Shift+P**, run **Attempt Update**, and restart when prompted. This doesn't work when `update.mode` is `none`, so download the installer instead.

The download page offers the latest release and a few recent ones. Versions that have aged out aren't available, so updating to the latest release is the way forward.

## How can admins keep their team on a supported Cursor version?

- **Push the latest build through MDM.** Download it from [cursor.com/download](https://cursor.com/download) and deploy it with your MDM tool (Jamf, Kandji, Intune, or similar).
- **Control automatic updates with `UpdateMode`.** Set the `UpdateMode` policy in your [MDM configuration](https://cursor.com/docs/enterprise/deployment-patterns.md#mdm-configuration) to choose how Cursor updates. If you turn automatic updates off, plan to push a new build regularly so your team stays ahead of the minimum versions.

## What are common questions about the minimum version policy?

### Why is my Cursor version blocked?

Your version is older than the minimum allowed version, which usually happens about 3 months after a release ships. Update to the latest version from [cursor.com/download](https://cursor.com/download) to keep using Cursor.

### What if I dismissed the Cursor update warning?

The warning comes back each time Cursor starts and after agent requests. Once your version reaches the minimum allowed version, agent requests fail with an "Update Required" error instead. Update any time before or after that point to clear it.

### What if my IT team controls Cursor updates?

Contact your IT admin and ask them to deploy the latest version. Admins can push it through MDM and manage automatic updates with the `UpdateMode` policy. See [How can admins keep their team on a supported Cursor version?](https://cursor.com/help/troubleshooting/minimum-version.md#how-can-admins-keep-their-team-on-a-supported-cursor-version)

### Will I lose my work when I update Cursor?

No. Chat history, settings, and other saved data stay on your machine and are available again after you update.

## Related

- [Minimum versions](https://cursor.com/docs/enterprise/deployment-patterns.md#minimum-versions)
- [MDM configuration](https://cursor.com/docs/enterprise/deployment-patterns.md#mdm-configuration)
- [Installation and startup](https://cursor.com/help/troubleshooting/install-issues.md)
- [Download and install](https://cursor.com/help/getting-started/install.md)


---

## Sitemap

[Overview of all docs pages](/llms.txt)
