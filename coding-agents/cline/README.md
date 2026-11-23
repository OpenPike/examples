# Cline through OpenPike

Cline's OpenAI Compatible provider takes a base URL, key and model. It has no header field, so create the virtual key with the tag `agent=cline`.

In Cline's settings:

- **API Provider:** OpenAI Compatible
- **Base URL:** `https://api.openpike.dev/v1`
- **API Key:** your OpenPike virtual key
- **Model ID:** `deepseek/deepseek-flash` (or an alias such as `openpike/auto`)

Check: give Cline a small task and find its requests in OpenPike Logs under `agent=cline`.

Docs: https://openpike.dev/docs/integrations/cline/
