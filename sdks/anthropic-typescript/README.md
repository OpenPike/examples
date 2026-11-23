# Anthropic SDK (TypeScript)

Streams a Claude message with `@anthropic-ai/sdk`. It sends `x-openpike-tags: agent=anthropic-typescript` so its spend shows per agent.

Env var: `OPENPIKE_API_KEY` (an OpenPike virtual key). Base URL: `https://api.openpike.dev (no /v1)`.

```bash
npm install   # once, in the repo root
export OPENPIKE_API_KEY=opk_live_...
npx tsx sdks/anthropic-typescript/stream.ts   # from the repo root
```

Docs: https://openpike.dev/docs/integrations/anthropic-sdk/
