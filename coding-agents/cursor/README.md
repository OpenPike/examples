# Cursor through OpenPike

Cursor has no config file for this; it is three settings. Chat models only, and OpenPike must be reachable from the internet (Cursor routes requests through its own servers).

1. Cursor Settings, Models, API Keys: paste your OpenPike virtual key into **OpenAI API Key**.
2. Turn on **Override OpenAI Base URL** and enter `https://api.openpike.dev/v1`.
3. Add a custom model named exactly as OpenPike names it, for example `deepseek/deepseek-flash`, and select it.

Cursor cannot send headers, so create the virtual key with the tag `agent=cursor`: the tag on the key attributes the spend.

Check: send a chat message, then find it in OpenPike Logs under `agent=cursor`.

Docs: https://openpike.dev/docs/integrations/cursor/
