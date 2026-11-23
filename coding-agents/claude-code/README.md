# Claude Code through OpenPike

Runs Claude Code against OpenPike's `/v1/messages` endpoint, so its spend has a budget, loop detection and an `agent=claude-code` tag.

Settings that matter:

- `ANTHROPIC_BASE_URL`: `https://api.openpike.dev` (Claude Code adds `/v1/messages`)
- `ANTHROPIC_AUTH_TOKEN`: your OpenPike virtual key
- `ANTHROPIC_CUSTOM_HEADERS`: `x-openpike-tags: agent=claude-code`

Run it: merge `settings.json` into `~/.claude/settings.json` (never a project's committed `.claude/settings.json`, which would share the key), then:

```bash
claude
```

Or for one shell session:

```bash
export ANTHROPIC_BASE_URL=https://api.openpike.dev
export ANTHROPIC_AUTH_TOKEN=opk_live_...
export ANTHROPIC_CUSTOM_HEADERS="x-openpike-tags: agent=claude-code"
claude
```

Check: `/status` shows the OpenPike base URL, and the request appears in OpenPike Logs with the agent `claude-code`.

Docs: https://openpike.dev/docs/integrations/claude-code/
