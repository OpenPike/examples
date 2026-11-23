# A budget per developer

Give each developer a virtual key with its own monthly budget, and a team budget on top. This is dashboard setup, so there is no code; `check.sh` shows the block when a developer reaches the hard limit.

1. **Keys**: one virtual key per developer with tags `dev=alice,team=platform`.
2. **Budgets**: per key, scope Virtual key, period Month, soft limit `$150`, hard limit `$200`.
3. **Budgets**: one more, scope Tag `team=platform`, period Month, hard limit `$1,500`.
4. **Alerts**: add an email or Slack channel and select Send test.

Env var: `OPENPIKE_API_KEY` (one developer's key).

```bash
export OPENPIKE_API_KEY=opk_live_...
./check.sh
```

Over the hard limit the request answers `429 budget_exceeded` with a `retry-after` header.

Docs: https://openpike.dev/docs/recipes/budget-per-developer/
