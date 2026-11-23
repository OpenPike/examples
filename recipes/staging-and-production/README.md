# Staging and production workspaces

Two workspaces, each with its own provider keys, virtual keys, budgets and alerts. The base URL is the same; only the virtual key differs, so the key decides the workspace.

1. An organization owner selects New workspace twice: `staging` and `production`.
2. Add provider keys and virtual keys in each. Staging gets a low daily hard budget, production a monthly budget plus loop limits.

Env vars: `OPENPIKE_API_KEY` (the environment's own key) and `APP_ENV` (`staging` or `production`, used as a tag).

```bash
cp .env.example .env   # fill in, one file per deployment
pip install -r ../../requirements.txt
python app.py
```

Docs: https://openpike.dev/docs/recipes/staging-and-production/
