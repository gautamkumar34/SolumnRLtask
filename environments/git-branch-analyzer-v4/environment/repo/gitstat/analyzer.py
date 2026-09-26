"""Report implementations for the gitstat CLI."""

from .utils import run_cmd


def list_branches():
    """Return the repo's branch names."""
    out = run_cmd("git branch --format='%(refname:short)'")
    return [b.strip() for b in out.splitlines() if b.strip()]


def list_authors():
    """Return the distinct commit author names."""
    out = run_cmd("git log --format='%an' | sort | uniq")
    return [a.strip() for a in out.splitlines() if a.strip()]


def activity():
    """Return commit counts per day, most active day first."""
    out = run_cmd("git log --format='%ad' --date=short | sort | uniq -c | sort -rn")
    return [line.rstrip() for line in out.splitlines() if line.strip()]


def log(rev, count=10):
    """Return the most recent commits on a revision, newest first."""
    out = run_cmd(f"git log --oneline -n {count} {rev}")
    return [line.rstrip() for line in out.splitlines() if line.strip()]


