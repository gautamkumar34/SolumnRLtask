"""Regression tests for the existing gitstat subcommands.

These build a throwaway git repo and exercise the CLI end to end. They must
keep passing after the new `summarize` command is added.
"""

import os
import shutil
import subprocess
import sys
import tempfile

import pytest


@pytest.fixture(scope="module")
def repo():
    d = tempfile.mkdtemp()

    def g(*a):
        subprocess.run(["git", *a], cwd=d, check=True, capture_output=True)

    g("init", "-q", "-b", "main")
    g("config", "user.name", "Ada Lovelace")
    g("config", "user.email", "ada@example.com")
    with open(os.path.join(d, "README.md"), "w") as f:
        f.write("# project\n")
    g("add", ".")
    g("commit", "-q", "-m", "Initial commit")
    with open(os.path.join(d, "config.txt"), "w") as f:
        f.write("config\n")
    g("add", ".")
    g("commit", "-q", "-m", "Add config")
    g("branch", "feature/login")
    yield d
    shutil.rmtree(d, ignore_errors=True)


def run(repo, *args):
    p = subprocess.run(
        [sys.executable, "-m", "gitstat", *args],
        cwd=repo,
        capture_output=True,
        text=True,
    )
    return p.stdout


def test_branches(repo):
    out = run(repo, "branches")
    assert "main" in out
    assert "feature/login" in out


def test_authors(repo):
    out = run(repo, "authors")
    assert "Ada Lovelace" in out


def test_activity(repo):
    out = run(repo, "activity")
    assert out.strip() != ""


def test_log(repo):
    out = run(repo, "log", "main")
    assert out.strip() != ""
