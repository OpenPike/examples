# LangChain (TypeScript)

Calls a chat model through `ChatOpenAI` from `@langchain/openai`. It sends `x-openpike-tags: agent=langchain-typescript` so its spend shows per agent.

Env var: `OPENPIKE_API_KEY` (an OpenPike virtual key). Base URL: `https://api.openpike.dev/v1`.

```bash
npm install   # once, in the repo root
export OPENPIKE_API_KEY=opk_live_...
npx tsx sdks/langchain-typescript/chat.ts   # from the repo root
```

Docs: https://openpike.dev/docs/integrations/langchain/
