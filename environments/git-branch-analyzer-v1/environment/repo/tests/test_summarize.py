"""Spec test for the new `summarize` command (currently failing)."""

import os
import shutil
import subprocess
import sys
import tempfile

import pytest


@pytest.fixture
def repo():
    d = tempfile.mkdtemp()

    def g(*a):
        subprocess.run(["git", *a], cwd=d, check=True, capture_output=True)

    g("init", "-q", "-b", "main")
    g("config", "user.name", "Ada Lovelace")
    g("config", "user.email", "ada@example.com")
    with open(os.path.join(d, "a.txt"), "w") as f:
        f.write("a\n")
    g("add", "."); g("commit", "-q", "-m", "Initial commit")
    with open(os.path.join(d, "b.txt"), "w") as f:
        f.write("b\n")
    g("add", "."); g("commit", "-q", "-m", "Add login form")
    g("tag", "v2.1.0")
    yield d
    shutil.rmtree(d, ignore_errors=True)


def run(repo, *args):
    return subprocess.run(
        [sys.executable, "-m", "gitstat", *args],
        cwd=repo, capture_output=True, text=True,
    ).stdout


# summarize should build its git command like the other rev-based commands —
# e.g. analyzer.log(rev) runs:  run_cmd(f"git log --oneline {rev}")
def test_summarize_tag(repo):
    out = run(repo, "summarize", "v2.1.0")
    assert "commits: 2" in out
    assert "latest: Add login form" in out
