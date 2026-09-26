#!/usr/bin/env bash
# Confirm the Solumn rollout endpoint is reachable and serving gpt-5.5.
# Reads creds from the .env beside the project root; never prints the key.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/../../.." && pwd)"   # -> SolumnRLtask/
if [ ! -f "$ROOT/.env" ]; then
  echo "Missing $ROOT/.env — create it with OPENAI_BASE_URL and OPENAI_API_KEY." >&2
  exit 1
fi
set -a; . "$ROOT/.env"; set +a

curl -s "$OPENAI_BASE_URL/chat/completions" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"messages":[{"role":"user","content":"Hi how are you"}]}' \
  | python3 -c 'import sys,json; d=json.load(sys.stdin); print("model:", d.get("model")); print("ok" if d.get("choices") else "NO choices")'
