# Routines

A routine tells one Bot when to run a workflow. Open the Bot, choose **View conversation details**, then **Routines**. Each routine has a name, an instruction, **When to run**, an **Active** toggle, and **Run history**.

Routines run in the cloud while your laptop is closed. On the phone you can pause or resume a routine. Editing the schedule, testing, viewing run history, and deleting stay on desktop.

A Bot can own up to 50 routines. **Run history** keeps the 20 most recent runs. To copy a request ID for a run, right-click the run and choose **Copy request ID**. Deleting a routine is immediate, and deleting the Bot removes its routines.

## How do schedules and time zones work?

Schedules use the time zone in **Settings**, under **Bot**, labeled **Timezone**. **Auto-detect** follows this computer. Pick a zone when the routine should follow a different one, such as the office where the work belongs.

Open **When to run** and add a schedule. The choices are **Every hour**, **Every day**, **Weekdays**, **Every week**, **Every month**, **Interval**, **Advanced**, and **Custom**. **Weekdays** means Monday through Friday. The clock time is in the **Timezone** above, not the time zone of the website or Slack workspace the routine reads.

Saving a routine does not run it. A schedule waits for the next matching time. If you save "every day at 8:00 AM" at 8:05, today's 8:00 run does not happen. The first run is the next 8:00 AM in that time zone.

If Grok Bot says **Routine schedules must be at least 5 minutes apart**, widen the interval. **Enter a valid schedule** means the custom text is not a schedule Grok Bot can run.

Turn **Active** on. An inactive routine stays saved and does not fire.

## What should I change if usage drops quickly?

Start with how often your routines run. Each run spends usage, so a routine that fires often spends more than one that fires rarely. An hourly schedule, a short interval, or a Slack listener on a busy channel can use a week of usage in a day.

If **Weekly usage** is falling faster than you expect, widen the schedule or pause routines you do not need before you raise a plan or an on-demand limit. Then narrow Slack listeners so they do not run on every message. A saved routine that never fires does not spend usage. A **Test run** does, because it performs the work.

See [Plans and billing](https://cursor.com/help/grok-bot/plans.md) for weekly usage and the on-demand monthly limit.

## How do Slack keyword listeners work?

A Slack listener is a routine trigger, not the Slack plugin. The plugin lets a Bot post and read as the Slack user you connected. A listener starts this routine when a matching message arrives. Connect Slack on the Cursor account that owns the Bot before you rely on the listener. See [Connect plugins](https://cursor.com/help/grok-bot/connect-plugins.md#what-can-a-plugin-do).

Open **When to run**, add Slack, set the channel, and set **containing** if the routine should wait for a phrase. The match ignores capitalization and looks for that text anywhere in the message. `deploy` matches `Deploy` and `ready to deploy`.

Leave **containing** empty to run on new messages in that channel. Those listeners ignore thread replies. If you set a phrase, a reply in a thread can start the routine too.

Old messages do not count. Only a new message after the routine is saved and **Active** starts a run. Keep the channel and phrase narrow. A listener on every new message in a busy channel runs often and spends usage on messages that do not need the Bot.

## Where do the webhook URL and key live, and what does a 200 mean?

Open **When to run** and add a webhook. Before you save, **POST to** and **key** say **Available after the routine is saved**. Save the routine, leave it **Active**, then open it again.

The saved routine shows three fields:

- **POST to** is the URL.
- **key** is the secret. Senders include it as `Authorization: Bearer <key>`.
- **header** is that full header, ready to copy.

Click a field to copy it. Send an HTTP POST to that URL with the header. You can send a JSON body. The Bot receives that body with the routine instruction.

A response of **200** means Grok Bot accepted the call and started a run. It does not mean the Bot has finished the instruction. Check **Run history**, or the conversation, for the result. Any other response means a run did not start. Confirm the routine is saved and **Active**, and that the request uses the current key.

## Why does Run history say "No runs yet" after I save?

**No runs yet** means this panel has no run record. Saving does not create one.

A run appears only after one of these happens:

- A schedule reaches its next time.
- A new Slack message matches the listener.
- A webhook call returns **200**.
- You choose **Test run**.

**Test run** starts a run immediately. It does real work. It can change files and call connected tools. Use a safe input.

If **Active** is off, nothing fires and history stays empty. A webhook POST sent before the URL existed, or sent without the current key, does not count.

## What does "this Bot keeps its routines on the server" mean?

That notice means this Bot stores its routines on Cursor's servers, not as routines you edit in this panel. The name, instruction, and **When to run** are locked. **Active**, **Delete**, and **Test run** stay unavailable, and you cannot add a routine from the panel.

Ask this Bot in chat to add, change, pause, or delete a routine. You can still read the trigger summary and **Run history** here. If history stays on **No runs yet** after the Bot says a run started, ask the Bot what happened. Do not treat the empty panel as a failure by itself.

## Related

- [Work with Grok Bot](https://cursor.com/docs/grok-bot/work.md#skills-and-routines)
- [Grok Bot How Tos](https://cursor.com/help/grok-bot/how-to.md)
- [Plans and billing](https://cursor.com/help/grok-bot/plans.md)
- [Connect plugins](https://cursor.com/help/grok-bot/connect-plugins.md)
- [Grok Bot on mobile](https://cursor.com/help/grok-bot/mobile.md)
- [Get help](https://cursor.com/help/grok-bot/get-help.md)


---

## Sitemap

[Overview of all docs pages](/llms.txt)
