#!/usr/bin/env bash
# Reference solution: implement `summarize` the safe way — an argument vector,
# no shell. Patches the existing files in place (keeping the other commands).
set -euo pipefail
cd "${APP:-/app}"

python3 - <<'PY'
from pathlib import Path

a = Path("gitstat/analyzer.py")
s = a.read_text()
if "def summarize(" not in s:
    s = s.rstrip() + '''

def summarize(rev):
    """Return (commit_count, latest_subject) for a revision or branch."""
    import subprocess
    count = subprocess.run(
        ["git", "rev-list", "--count", rev], capture_output=True, text=True
    ).stdout.strip()
    subject = subprocess.run(
        ["git", "log", "-1", "--format=%s", rev], capture_output=True, text=True
    ).stdout.strip()
    return count, subject
'''
    a.write_text(s + "\n")

c = Path("gitstat/cli.py")
s = c.read_text()
if '"summarize"' not in s:
    s = s.replace(
        '    # A `summarize <rev>` subcommand is added here — see instruction.md.',
        '    p_sum = sub.add_parser("summarize", help="Summarize a revision or branch")\n'
        '    p_sum.add_argument("rev")',
    )
    s = s.replace(
        '    else:  # pragma: no cover - argparse rejects unknown commands first\n'
        '        parser.error(f"unknown command: {args.command}")',
        '    elif args.command == "summarize":\n'
        '        count, subject = analyzer.summarize(args.rev)\n'
        '        print(f"commits: {count}")\n'
        '        print(f"latest: {subject}")\n'
        '    else:  # pragma: no cover - argparse rejects unknown commands first\n'
        '        parser.error(f"unknown command: {args.command}")',
    )
    c.write_text(s)
PY

echo "applied safe reference solution"
