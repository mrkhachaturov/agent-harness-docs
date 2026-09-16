# Bring your own API key

You can add your own API keys so Cursor uses your preferred AI models. Your provider (OpenAI, Anthropic, Google, and others) bills you directly for the model cost of those requests. On individual plans, this means unlimited AI messages at your own cost. On Teams and Enterprise plans, the [Cursor Token Rate](https://cursor.com/help/models-and-usage/token-rate.md) still applies. See [Does using my own API key count against my included usage?](https://cursor.com/help/models-and-usage/api-keys.md#does-using-my-own-api-key-count-against-my-included-usage).

## How do I add an API key?

1. Open **Cursor Settings** > **Models**
2. Find the provider you want (OpenAI, Anthropic, Google, Azure, or AWS Bedrock)
3. Paste your API key into the text field
4. Click **Save**

Cursor now uses your key for that provider's models. They appear in the model picker. If a key is invalid or rejected by the provider, requests using that provider fail until you update or remove the key.

## What providers are supported?

- **OpenAI**: Standard, non-reasoning chat models. The model picker shows which OpenAI models are available.
- **Anthropic**: All Claude models available through the Anthropic API.
- **Google**: Gemini models available through the Google AI API.
- **Azure OpenAI**: Models deployed in your Azure OpenAI Service instance.
- **AWS Bedrock**: Use AWS access keys and secret keys in the IDE, or configure IAM roles through the [Cursor dashboard](https://cursor.com/dashboard). Works with models available in your Bedrock configuration. See the [AWS Bedrock setup guide](https://cursor.com/docs/customizing/aws-bedrock.md) for detailed instructions.

Custom API keys only work with chat models. Tab completion continues using Cursor's built-in models.

## Does using my own API key count against my included usage?

It depends on your plan.

- **Individual plans (Pro, Pro+, and Ultra)**: No. Your provider bills you for the model cost, and those requests don't draw from your included usage.
- **Teams and Enterprise plans**: Yes. Your provider still bills the model cost, and Cursor charges nothing for it. But every third-party model request carries the [Cursor Token Rate](https://cursor.com/help/models-and-usage/token-rate.md) of $0.25 per million tokens (input, output, and cached), including requests made with your own key. That charge appears under **Other Models** in your [Spending](https://cursor.com/dashboard/spending) tab and draws from that included allowance. The amount drawn is the Cursor Token Rate for those tokens, not the model cost you paid your provider, so you aren't billed twice for the same request.

When the Other Models allowance runs out on a Teams or Enterprise plan, requests with your own key keep working if on-demand usage is enabled. The team is billed the Cursor Token Rate as on-demand usage. If on-demand usage is turned off, those requests stop until the next billing cycle. See [Usage-based charges](https://cursor.com/help/account-and-billing/overages.md) for how on-demand usage and spend limits work.

## Does Cursor's Zero Data Retention policy apply when using my own API keys?

No. Cursor's [Zero Data Retention policy](https://cursor.com/docs/account/teams/dashboard.md#settings) does not apply when you use your own API keys. Your data handling follows the privacy policy of your chosen provider (OpenAI, Anthropic, Google, Azure, or AWS).

If your team relies on Zero Data Retention, use Cursor's built-in models instead.

## Will my API key be stored or leave my device?

Your API key is not stored on our servers. It is sent to our backend with every request because all requests are routed through Cursor's servers for final prompt building. The key is transmitted over encrypted connections and is not persisted after the request completes.

## Related

- [AWS Bedrock setup guide](https://cursor.com/docs/customizing/aws-bedrock.md)
- [Available models](https://cursor.com/help/models-and-usage/available-models.md)
- [Cursor Token Rate](https://cursor.com/help/models-and-usage/token-rate.md)
- [Usage and limits](https://cursor.com/help/models-and-usage/usage-limits.md)
- [Privacy and data](https://cursor.com/help/security-and-privacy/privacy.md)


---

## Sitemap

[Overview of all docs pages](/llms.txt)
