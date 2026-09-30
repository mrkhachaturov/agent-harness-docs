# Installation and startup

Common problems when installing, launching, or updating Cursor.

## What if I see a blank screen on startup?

- Quit and restart Cursor
- On Mac, drag Cursor to Trash and reinstall from [cursor.com/download](https://cursor.com/download)
- On Windows, run Cursor as administrator
- Fully quit Cursor (Cmd+Q on Mac, or exit from the tray on Windows and Linux) and reopen it

## How do I update Cursor?

From inside Cursor: press **Cmd/Ctrl+Shift+P**, type **"Cursor: Attempt Update"**, and restart when prompted.

## What are update channels?

- **Stable** (default): recommended for most users
- **Early Access**: pre-release builds with the latest features, may be less stable

Switch channels in **Cursor Settings**.

## What does the macOS "Cursor is damaged" warning mean?

This is a macOS issue, not a corrupted download. To fix it:

First, quit Cursor and force-quit any remaining processes in Activity Monitor. Wait a minute, then reopen Cursor.

If the warning persists:

1. Move Cursor to Trash and empty the Trash. Re-download from [cursor.com/download](https://cursor.com/download)
2. If it still appears, restart your Mac and try again

## How do I free up disk space used by Cursor?

Cursor stores agent chat history, worktrees, and extensions locally. For most users the largest contributor is stored Cursor Agent conversations, not extensions.

### Clean up agent chat history

Old Cursor Agent chats accumulate in a local database that can grow to many gigabytes. Two commands work together to remove entries and reclaim the disk they were using. Run them in order. The second command is what actually shrinks the database file, and each one can take a minute or two on large databases.

From either the Agents Window or the classic editor window:

1. Open the Command Palette with `Cmd/Ctrl+Shift+P`
2. Run **Delete Old Chats…** and pick a retention window (for example, 30 days)
3. Then run **GC Agent KV Blobs**

Running Delete Old Chats on its own often removes the entries but leaves the file the same size on disk. GC Agent KV Blobs is what compacts the file back down.

### Tune worktree cleanup

If you use Cursor Agent, generated worktrees under `~/.cursor/worktrees/` can add up. Cursor cleans them up automatically, and you can adjust the limits.

From the **Agents Window**, open **Settings → Worktrees → Cleanup**. Two controls are available:

- **Max Worktrees** (default 25): the maximum number of Cursor-managed worktrees to retain across all workspaces. Older worktrees are removed first.
- **Max Total Size (GB)** (default 50): the maximum combined size across all Cursor-managed worktrees. Set to 0 to disable the size cap.

The same page lists every Cursor-managed worktree currently on your machine, grouped by source repository, with a delete button next to each so you can remove specific ones without waiting for automatic cleanup.

To change these from the **classic editor window**, open **VS Code Settings** with `Shift+Cmd/Ctrl+,` and search for `worktree`. Three settings are available:

- `cursor.worktreeMaxCount` (default 25)
- `cursor.worktreesGlobalMaxSizeGb` (default 50)
- `cursor.worktreeCleanupIntervalHours` (default 6): how often the background cleanup runs. This setting is only exposed in VS Code Settings, not in the Agents Window's settings UI.

### Remove unused extensions

To see what is currently loaded from either the Agents Window or the classic editor window, open the Command Palette with `Cmd/Ctrl+Shift+P` and run **Show Running Extensions**. This opens a diagnostic view listing every loaded extension along with its CPU and memory usage.

To uninstall an extension, use the classic editor window's Extensions sidebar. Open it with `Cmd/Ctrl+Shift+X`, right-click any extension you no longer need, and choose **Uninstall**.

## Related

- [Download and install](https://cursor.com/help/getting-started/install.md)
- [Reporting a bug](https://cursor.com/help/troubleshooting/reporting-bugs.md)


---

## Sitemap

[Overview of all docs pages](/llms.txt)
