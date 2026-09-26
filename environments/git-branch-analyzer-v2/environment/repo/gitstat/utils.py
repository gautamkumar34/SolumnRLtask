"""Command helpers used across the analyzer.

The analyzer talks to git a lot. Most calls are small, but a couple of the
reports (author de-duplication, activity roll-ups) are easiest to express as a
shell pipeline, so the shared helper below takes a full command line.
"""

import subprocess


def run_cmd(cmd, cwd=None):
    """Run a git command line and return its stdout.

    Accepts a full command string so that reports using pipes (``sort``,
    ``uniq``) work the same way as the simple ones.
    """
    proc = subprocess.run(
        cmd,
        shell=True,
        cwd=cwd,
        capture_output=True,
        text=True,
    )
    return proc.stdout
