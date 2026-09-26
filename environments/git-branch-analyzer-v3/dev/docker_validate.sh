#!/usr/bin/env bash
# Container-parity validation: build the pinned image and confirm the grader
# discriminates the three states inside the real environment (no Harbor needed).
#
#   seed   -> reward 0   safe -> reward 1   unsafe -> reward 0
set -euo pipefail

ENV_DIR="$(cd "$(dirname "$0")/.." && pwd)"
IMG="solumn/git-branch-analyzer:latest"

docker build -t "$IMG" "$ENV_DIR/environment"

grade_in_container() {
  # $1 = optional setup script on host to copy in and run before grading
  local setup="${1:-}"
  local cid
  cid=$(docker run -d --network none "$IMG" sleep 900)
  docker cp "$ENV_DIR/tests/." "$cid:/tests/" >/dev/null
  if [ -n "$setup" ]; then
    docker cp "$setup" "$cid:/tmp/setup.sh" >/dev/null
    docker exec -u root "$cid" bash /tmp/setup.sh >/dev/null
  fi
  docker exec -u root "$cid" bash -lc 'mkdir -p /logs/verifier && python3 /tests/grader.py >/dev/null 2>&1; cat /logs/verifier/reward.txt'
  docker rm -f "$cid" >/dev/null
}

fail=0
check() { if [ "$2" = "$3" ]; then echo "[PASS] $1 (reward $3)"; else echo "[FAIL] $1 expected $2 got $3"; fail=1; fi; }

echo "== seed =="
r=$(grade_in_container "");                              check seed   0 "$r"
echo "== safe =="
r=$(grade_in_container "$ENV_DIR/solution/solve.sh");    check safe   1 "$r"
echo "== unsafe =="
r=$(grade_in_container "$ENV_DIR/dev/unsafe_solve.sh");  check unsafe 0 "$r"

[ "$fail" = 0 ] && echo "CONTAINER VALIDATION PASSED" || { echo "FAILED"; exit 1; }
