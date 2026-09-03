# SSO and authentication

SSO with SAML 2.0 is available at no additional cost on Teams and Enterprise plans. Where you configure it depends on whether you use team-level or org-level SSO.

## What do I need before setting up SSO?

- A Cursor Teams or Enterprise plan
- Admin access to your identity provider (e.g., Okta, Azure AD, Google Workspace)
- Admin access to your Cursor team (Teams) or organization (Enterprise)

## Where do I configure SSO?

- **Teams:** Open [Single Sign-On (SSO) settings](https://cursor.com/dashboard/team-settings#single-sign-on-sso) in Team Settings.
- **Enterprise:** Open the Organization's Settings. Org-level SSO is configured there, not in Team Settings. See [Organizations](https://cursor.com/docs/enterprise/organizations.md#identity-model).

Team-level SSO stays available for a team that needs its own identity provider. Most Enterprise orgs should use org-level SSO.

## How do I set up SSO?

For team-level SSO, follow the [SSO setup reference](https://cursor.com/docs/account/teams/sso.md). You'll need admin access to both your identity provider and your Cursor team.

For org-level SSO on Enterprise, set up the connection in the Organization's Settings. See [Organizations](https://cursor.com/docs/enterprise/organizations.md#identity-model) and [Identity and access management](https://cursor.com/docs/enterprise/identity-and-access-management.md#single-sign-on-sso-and-saml).

## Does Cursor support SCIM provisioning?

Yes, on Enterprise plans with SSO enabled. SCIM automatically manages team members through your identity provider, keeping your Cursor team in sync with your organization.

## How do I view my SSO configuration and domains?

For team-level SSO, team admins can review the connection status and its domain in [Single Sign-On (SSO) settings](https://cursor.com/dashboard/team-settings#single-sign-on-sso). Click "Configure" next to "SSO-Provider Connection Settings" to view the provider connection details. Click "Configure" next to "Domain Verification Settings" to view or manage verified domains.

For org-level SSO, org admins review the connection in the Organization's Settings. See [Organizations](https://cursor.com/docs/enterprise/organizations.md#identity-model).

## Why do team members see "Not assigned to this application"?

This means the team member hasn't been assigned to the Cursor application in your identity provider's admin console. Add them to the Cursor app in your IdP to fix this.

## Related

- [SSO reference](https://cursor.com/docs/account/teams/sso.md)
- [Organizations](https://cursor.com/docs/enterprise/organizations.md)
- [Identity and access management](https://cursor.com/docs/enterprise/identity-and-access-management.md)
- [Set up a team](https://cursor.com/help/account-and-billing/teams-setup.md)


---

## Sitemap

[Overview of all docs pages](/llms.txt)
