# OpenAI SDK (TypeScript)

Streams a chat completion with the official `openai` package. It sends `x-openpike-tags: agent=openai-typescript` so its spend shows per agent.

Env var: `OPENPIKE_API_KEY` (an OpenPike virtual key). Base URL: `https://api.openpike.dev/v1`.

```bash
npm install   # once, in the repo root
export OPENPIKE_API_KEY=opk_live_...
npx tsx sdks/openai-typescript/stream.ts   # from the repo root
```

Docs: https://openpike.dev/docs/integrations/openai-sdk/
