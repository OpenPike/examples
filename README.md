# OpenPike examples

Copy-paste setups for using [OpenPike](https://openpike.dev) with coding agents, SDKs and frameworks, plus recipes for budgets, loop protection, fallbacks and separate environments. Every example sends `x-openpike-tags` (or has you tag the key) so spend shows per agent.

You need an OpenPike virtual key (`opk_live_...`) and a provider key added to your workspace. Each folder has a README with its env vars and exact command, and a `.env.example`. Docs: https://openpike.dev/docs/

## Coding agents

| Example | Docs page |
| --- | --- |
| [Claude Code](coding-agents/claude-code) | [integration](https://openpike.dev/docs/integrations/claude-code/) |
| [Cursor](coding-agents/cursor) | [integration](https://openpike.dev/docs/integrations/cursor/) |
| [opencode](coding-agents/opencode) | [integration](https://openpike.dev/docs/integrations/opencode/) |
| [Cline](coding-agents/cline) | [integration](https://openpike.dev/docs/integrations/cline/) |
| [Aider](coding-agents/aider) | [integration](https://openpike.dev/docs/integrations/aider/) |
| Codex CLI | coming with `/v1/responses` support in these examples |

## SDKs and frameworks

| Example | Docs page |
| --- | --- |
| [OpenAI SDK, Python](sdks/openai-python) | [integration](https://openpike.dev/docs/integrations/openai-sdk/) |
| [OpenAI SDK, TypeScript](sdks/openai-typescript) | [integration](https://openpike.dev/docs/integrations/openai-sdk/) |
| [Anthropic SDK, Python](sdks/anthropic-python) | [integration](https://openpike.dev/docs/integrations/anthropic-sdk/) |
| [Anthropic SDK, TypeScript](sdks/anthropic-typescript) | [integration](https://openpike.dev/docs/integrations/anthropic-sdk/) |
| [Vercel AI SDK](sdks/vercel-ai-sdk) | [integration](https://openpike.dev/docs/integrations/vercel-ai-sdk/) |
| [LangChain, Python](sdks/langchain-python) | [integration](https://openpike.dev/docs/integrations/langchain/) |
| [LangChain, TypeScript](sdks/langchain-typescript) | [integration](https://openpike.dev/docs/integrations/langchain/) |
| [LlamaIndex](sdks/llamaindex) | [integration](https://openpike.dev/docs/integrations/llamaindex/) |

## Recipes

| Example | Docs page |
| --- | --- |
| [A budget per developer](recipes/budget-per-developer) | [recipe](https://openpike.dev/docs/recipes/budget-per-developer/) |
| [Stop a runaway agent](recipes/stop-a-runaway-agent) | [recipe](https://openpike.dev/docs/recipes/stop-a-runaway-agent/) |
| [A cheap fallback chain](recipes/cheap-fallback-chain) | [recipe](https://openpike.dev/docs/recipes/cheap-fallback-chain/) |
| [Staging and production](recipes/staging-and-production) | [recipe](https://openpike.dev/docs/recipes/staging-and-production/) |

## Checks

CI lints and typechecks every TypeScript and Python example on each pull request. A live job runs the SDK examples against `https://api.openpike.dev` when the repo secret `OPENPIKE_API_KEY` is set (use a dedicated virtual key with a small hard budget).

Licensed under MIT. Security reports: see [SECURITY.md](SECURITY.md).
