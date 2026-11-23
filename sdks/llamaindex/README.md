# LlamaIndex

Calls a chat model through `OpenAILike` pointed at OpenPike. It sends `x-openpike-tags: agent=llamaindex` so its spend shows per agent.

Env var: `OPENPIKE_API_KEY` (an OpenPike virtual key). Base URL: `https://api.openpike.dev/v1`.

```bash
pip install -r ../../requirements.txt
export OPENPIKE_API_KEY=opk_live_...
python chat.py
```

Docs: https://openpike.dev/docs/integrations/llamaindex/
