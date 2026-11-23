#!/usr/bin/env bash
# One tagged request with the developer's key; prints the status and OpenPike's headers.
set -euo pipefail
curl -sS -D - -o /dev/null https://api.openpike.dev/v1/chat/completions \
  -H "Authorization: Bearer ${OPENPIKE_API_KEY:?set OPENPIKE_API_KEY}" \
  -H "Content-Type: application/json" \
  -H "x-openpike-tags: dev=alice,team=platform" \
  -d '{"model":"deepseek/deepseek-flash","messages":[{"role":"user","content":"Say hi."}]}' \
  | grep -i -E '^(HTTP|x-openpike|retry-after)'
