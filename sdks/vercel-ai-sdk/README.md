# Vercel AI SDK

Calls an OpenAI-format model with `createOpenAI` (using `.chat()`) and a Claude model with `createAnthropic`. It sends `x-openpike-tags: agent=vercel-ai-sdk` so its spend shows per agent.

Env var: `OPENPIKE_API_KEY` (an OpenPike virtual key). Base URL: `https://api.openpike.dev/v1 (both providers)`.

```bash
npm install   # once, in the repo root
export OPENPIKE_API_KEY=opk_live_...
npx tsx sdks/vercel-ai-sdk/generate.ts   # from the repo root
```

Docs: https://openpike.dev/docs/integrations/vercel-ai-sdk/
