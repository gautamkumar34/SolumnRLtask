"""Legacy helpers retained for the migration tooling."""

from .utils import run_cmd


def rev_git(rev, subcmd):
    """Run a git subcommand against a revision.

    e.g. rev_git(rev, "rev-list --count") or rev_git(rev, "log -1 --format=%s").
    """
    return run_cmd(f"git {subcmd} {rev}")
