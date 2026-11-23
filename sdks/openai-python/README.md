# OpenAI SDK (Python)

Streams a chat completion with the official `openai` package. It sends `x-openpike-tags: agent=openai-python` so its spend shows per agent.

Env var: `OPENPIKE_API_KEY` (an OpenPike virtual key). Base URL: `https://api.openpike.dev/v1`.

```bash
pip install -r ../../requirements.txt
export OPENPIKE_API_KEY=opk_live_...
python stream.py
```

Docs: https://openpike.dev/docs/integrations/openai-sdk/
