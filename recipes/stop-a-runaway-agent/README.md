# Stop a runaway agent

`loop.py` is a deliberate loop: it sends the same request again and again with the tag `agent=runaway-demo` and a run ID, so loop detection or a run budget stops it. It stops itself on the first `429` (and sets `max_retries=0`, because retrying does not help).

Set up first (Budgets page, plan Team or Business for loop limits):

1. A budget with scope Tag `agent=runaway-demo`, requests per minute `20`, pause `300` seconds.
2. Optionally run limits on the same budget: `$0.50` and `30` requests per run.
3. Alerts: add your email and select Send test.

Env var: `OPENPIKE_API_KEY`. Use a key with a small hard budget, since this spends real tokens.

```bash
pip install -r ../../requirements.txt
export OPENPIKE_API_KEY=opk_live_...
python loop.py
```

Expect `loop_detected` (a pause) or `run_limit_exceeded` (the run cap) within a minute. Resume on the Agents page.

Docs: https://openpike.dev/docs/recipes/stop-a-runaway-agent/
