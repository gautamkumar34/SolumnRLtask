#!/usr/bin/env bash
# One-shot: load the rollout creds, (re)build the environment images, and run
# GPT-5.5 against each seed. Safe under both bash and zsh.
#
# Usage:  bash run_rollouts.sh [N_ROLLOUTS] [env-id ...]
#   N_ROLLOUTS  rollouts per environment (default 4)
#   env-id ...  which environments to run (default: both seeds)
set -euo pipefail

ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT"

if [ ! -f "$ROOT/.env" ]; then
  echo "Missing $ROOT/.env (needs OPENAI_BASE_URL and OPENAI_API_KEY)." >&2
  exit 1
fi
set -a; . "$ROOT/.env"; set +a
: "${OPENAI_BASE_URL:?not set — check .env}" "${OPENAI_API_KEY:?not set — check .env}"

N="${1:-4}"; shift || true
ENVS=("$@")
if [ "${#ENVS[@]}" -eq 0 ]; then
  # default: every environment under environments/
  ENVS=()
  for d in environments/*/; do ENVS+=("$(basename "$d")"); done
fi

RUN="rollouts_$(date +%Y%m%d_%H%M%S)"

for id in "${ENVS[@]}"; do
  echo "==== building image: solumn/$id:latest ===="
  docker build -t "solumn/$id:latest" "environments/$id/environment"
  echo "==== rollout: $id  (n=$N, job=$RUN) ===="
  harbor run -p environments -i "$id" -a terminus-2 -m openai/gpt-5.5 \
    -k 6 -o "jobs/$id" --job-name "$RUN" -n "$N" --yes
done

echo
echo "Done. Result files:"
for id in "${ENVS[@]}"; do echo "  jobs/$id/$RUN/result.json"; done
