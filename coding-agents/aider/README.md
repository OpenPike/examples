# Aider through OpenPike

Aider reads two environment variables for any OpenAI-compatible endpoint. Create the virtual key with the tag `agent=aider` (Aider sends no tag header).

Env vars: `OPENAI_API_BASE`, `OPENAI_API_KEY`.

```bash
export OPENAI_API_BASE=https://api.openpike.dev/v1
export OPENAI_API_KEY=opk_live_...
aider --model openai/deepseek/deepseek-flash
```

The `openai/` prefix tells Aider the endpoint type; the rest is the OpenPike model name. Aider warns about models it does not know; that is expected.

Docs: https://openpike.dev/docs/integrations/aider/
