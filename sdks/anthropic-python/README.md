# Anthropic SDK (Python)

Streams a Claude message with the official `anthropic` package. It sends `x-openpike-tags: agent=anthropic-python` so its spend shows per agent.

Env var: `OPENPIKE_API_KEY` (an OpenPike virtual key). Base URL: `https://api.openpike.dev (no /v1)`.

```bash
pip install -r ../../requirements.txt
export OPENPIKE_API_KEY=opk_live_...
python stream.py
```

Docs: https://openpike.dev/docs/integrations/anthropic-sdk/
