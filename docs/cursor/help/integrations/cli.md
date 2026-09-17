# CLI

Ship code with AI agents right from your terminal.

## How do I install the CLI?

```bash
curl https://cursor.com/install -fsS | bash
```

On Windows PowerShell:

```powershell
irm 'https://cursor.com/install?win32=true' | iex
```

## What can the CLI do?

The CLI brings Cursor's AI capabilities to your terminal. It supports Agent, Plan, and Ask modes for interactive coding and automation. Some features work differently or are available only in the editor.

Learn more at [cursor.com/cli](https://cursor.com/cli).

## Can I use the CLI for automation?

Yes. Use headless mode for scripts, CI pipelines, and [GitHub Actions](https://cursor.com/docs/cli/github-actions.md). Automate doc updates, trigger security reviews, or build custom coding workflows. See the [Headless CLI docs](https://cursor.com/docs/cli/headless.md) for setup.

## Does the CLI work with other editors?

Yes. Cursor CLI works with any IDE or editor. Plug it into your existing workflow anywhere you have a terminal.

## How do I authenticate the CLI?

Run `agent login` or set the `CURSOR_API_KEY` environment variable. See the [CLI authentication docs](https://cursor.com/docs/cli/reference/authentication.md) for details.

## What if the CLI can't reach Cursor's servers?

Check your network connection first. Behind a VPN or firewall, allowlist `*.cursor.sh` and `*.cursorapi.com`. For proxy environment variables and HTTP/1.1 fallback, see [CLI configuration](https://cursor.com/docs/cli/reference/configuration.md).

## How do I update the CLI?

Cursor CLI auto-updates by default. To update manually, run:

```bash
agent update
```

## Related

- [CLI overview](https://cursor.com/docs/cli/overview.md)
- [CLI installation](https://cursor.com/docs/cli/installation.md)
- [CLI authentication](https://cursor.com/docs/cli/reference/authentication.md)
- [CLI configuration](https://cursor.com/docs/cli/reference/configuration.md)
- [GitHub Actions](https://cursor.com/docs/cli/github-actions.md)
- [cursor.com/cli](https://cursor.com/cli)


---

## Sitemap

[Overview of all docs pages](/llms.txt)
