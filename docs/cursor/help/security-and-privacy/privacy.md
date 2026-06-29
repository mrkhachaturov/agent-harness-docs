# Privacy and data

Cursor is designed to keep your code private. Here's how data handling works.

## What is Privacy Mode?

Privacy Mode ensures your code is never used for training by Cursor or other AI model providers.

Learn more about [how your data is used](https://cursor.com/data-use).

For more information about subprocessors and data handling, see the [Security page](https://cursor.com/security#infrastructure-security).

## How do I enable Privacy Mode?

1. Open Cursor Settings:
   - **Mac**: Press Cmd + Shift + J
   - **Windows/Linux**: Press Ctrl + Shift + J
2. Click **General** in the sidebar
3. Toggle **Privacy Mode** on

For teams, Privacy Mode is enabled by default for all team members. Admins can enforce it organization-wide via [cursor.com/dashboard](https://cursor.com/dashboard) so members cannot disable it.

## What data is sent to AI providers?

When you use AI features, Cursor sends prompts and code context to model providers like OpenAI, Anthropic, and Google. With Privacy Mode enabled, your code is not used for training.

## Where is my code processed?

When you use AI features, Cursor sends prompts and code context to model providers like OpenAI, Anthropic, and Google. All [sub-processors](https://trust.cursor.com/subprocessors) have data processing agreements.

See the [Security page](https://cursor.com/security#infrastructure-security) for details.

## Is my code used for training?

With Privacy Mode enabled, your code is never used for training.

Privacy Mode is on by default for Enterprise teams. Teams and Enterprise admins can enforce it organization-wide so members cannot disable it.

## Are there exceptions to zero data retention?

ZDR doesn't apply when you use your own API keys. In that case, your data handling follows your provider's privacy policy.

Some models also require data retention with their provider and fall outside Cursor's ZDR agreements. These models are off by default and require admin approval before use. See [Models with data retention](https://cursor.com/docs/enterprise/privacy-and-data-governance.md#models-with-data-retention) for details.

## What privacy controls are available for enterprise?

Enterprise plans include additional controls beyond Privacy Mode:

- **AI code tracking API and audit logs**: Track how AI features are used across your organization
- **Granular admin and model controls**: Restrict model access, enforce Privacy Mode org-wide, and manage agent permissions
- **Compliance certifications**: SOC 2 Type II and more (see [Security and compliance documents](https://cursor.com/help/security-and-privacy/compliance.md))
- **Customer Managed Encryption Keys (CMEK)**: Encrypt embeddings and Cloud Agent data with your own keys, with full control over key rotation and access

See the full Enterprise feature list on [cursor.com/pricing](https://cursor.com/pricing) or [contact sales](https://cursor.com/contact-sales?source=docs-help-privacy) for details.

## Related

- [Security and compliance documents](https://cursor.com/help/security-and-privacy/compliance.md)
- [Privacy and data governance](https://cursor.com/docs/enterprise/privacy-and-data-governance.md)
- [Agent security](https://cursor.com/docs/agent/security.md)
- [API keys](https://cursor.com/help/models-and-usage/api-keys.md)


---

## Sitemap

[Overview of all docs pages](/llms.txt)
