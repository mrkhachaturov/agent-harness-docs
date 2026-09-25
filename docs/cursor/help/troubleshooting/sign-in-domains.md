# Which domains does Cursor sign-in need?

On September 30, Cursor sign-in moves to accounts.spacex.ai and accounts.x.ai (replacing authenticator.cursor.sh as the sign-in page). Your Cursor app, site, and SSO tiles keep working, and nobody gets logged out.

If your company uses a firewall or proxy allowlist (for example Zscaler), add the domains below. You have until October 30: if accounts.spacex.ai or accounts.x.ai are blocked on your network, sign-in falls back to the old page until then, so nobody is locked out on September 30.

We recommend adding the domains as soon as you can so your users get the new sign-in page from day one. After October 30, the fallback is retired and sign-in requires accounts.spacex.ai and accounts.x.ai.

If your team has bookmarks or internal docs that point to authenticator.cursor.sh, update them to accounts.spacex.ai and accounts.x.ai.

***

## Prefer wildcards

Use wildcards when you can, so you do not have to update the list later:

- `*.spacex.ai` (covers accounts.spacex.ai and related auth hosts)
- `*.x.ai` (covers accounts.x.ai, auth.x.ai, and related auth hosts)
- `*.grok.com` (covers auth.grok.com and grok.com)
- `*.grokusercontent.com` (covers auth.grokusercontent.com; serves user-generated Grok content)
- `*.grokipedia.com` (covers auth.grokipedia.com; Grokipedia shares Grok accounts)

## Minimum hosts

If your policy will not allow wildcards, allow at least:

- `accounts.x.ai`
- `accounts.spacex.ai`
- `auth.x.ai`
- `auth.grok.com`
- `auth.grokusercontent.com`
- `auth.grokipedia.com`

## Still required for Cursor itself

These are unchanged:

- `.cursor.sh` (includes authenticator.cursor.sh)
- `.cursor-cdn.com`
- `.cursorapi.com`
- `.cursorvm.com` and `.*.cursorvm.com`

## Notes for IT / admins

- Existing Cursor sessions stay signed in. This is not a forced logout
- SSO IdP config (Okta tiles, ACS URLs, and similar) does not need to change for this change
- Cursor app, website, and API hosts (cursor.com, api\*.cursor.com) are not changing

If login fails after Sep 30 and your network uses an allowlist, have IT add the domains above, then retry from accounts.spacex.ai or accounts.x.ai, or your existing IDP / authenticator.cursor.sh.

## Related

- [Network, proxy, and remote connections](https://cursor.com/help/troubleshooting/network.md)
- [Network configuration](https://cursor.com/docs/enterprise/network-configuration.md)


---

## Sitemap

[Overview of all docs pages](/llms.txt)
