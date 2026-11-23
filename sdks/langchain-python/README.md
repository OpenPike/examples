# LangChain (Python)

Calls a chat model through `ChatOpenAI` pointed at OpenPike. It sends `x-openpike-tags: agent=langchain-python` so its spend shows per agent.

Env var: `OPENPIKE_API_KEY` (an OpenPike virtual key). Base URL: `https://api.openpike.dev/v1`.

```bash
pip install -r ../../requirements.txt
export OPENPIKE_API_KEY=opk_live_...
python chat.py
```

Docs: https://openpike.dev/docs/integrations/langchain/
