# OpenCode through OpenPike

Adds OpenPike to OpenCode as a custom OpenAI-compatible provider, with the tag `agent=opencode` on every request.

Env var: `OPENPIKE_API_KEY` (an OpenPike virtual key).

```bash
export OPENPIKE_API_KEY=opk_live_...
cp opencode.jsonc /path/to/your/project/opencode.jsonc   # or merge it into OpenCode's global config
opencode
```

Pick `openpike/deepseek-flash` with `/models`. Claude models are not available here: OpenPike serves them in the Anthropic format only.

Docs: https://openpike.dev/docs/integrations/opencode/
