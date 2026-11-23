# A cheap fallback chain

An alias lists models from different providers, tried in order, so the service keeps answering when one provider fails.

1. **Providers**: add a key for DeepSeek, Google AI Studio and OpenAI.
2. **Routing**: create the alias `fast`, format chat completions, policy `ordered`, targets `deepseek/deepseek-flash`, `google-ai-studio/gemini-3.6-flash`, `openai/gpt-5.4-mini`.
3. Use `openpike/fast` as the model.

Env var: `OPENPIKE_API_KEY`.

```bash
pip install -r ../../requirements.txt
export OPENPIKE_API_KEY=opk_live_...
python fallback.py
```

It prints which model answered and how many attempts it took (`x-openpike-model`, `x-openpike-attempts`).

Docs: https://openpike.dev/docs/recipes/cheap-fallback-chain/
