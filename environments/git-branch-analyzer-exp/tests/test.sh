#!/usr/bin/env bash
# Harbor verifier entrypoint. Runs after the agent stops and writes the reward
# to /logs/verifier/reward.txt (plus result.json with the per-check detail).
set -u

mkdir -p /logs/verifier
python3 /tests/grader.py
