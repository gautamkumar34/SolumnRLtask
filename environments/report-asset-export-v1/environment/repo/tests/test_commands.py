"""Regression tests for the existing assetsvc subcommands.

They build a throwaway asset store and exercise the CLI end to end. They must
keep passing after the new `export` command is added.
"""

import os
import shutil
import subprocess
import sys
import tempfile

import pytest


@pytest.fixture(scope="module")
def store():
    d = tempfile.mkdtemp()
    os.makedirs(os.path.join(d, "2024", "q3"))
    with open(os.path.join(d, "overview.txt"), "w") as f:
        f.write("Company overview\n")
    with open(os.path.join(d, "2024", "q3", "summary.txt"), "w") as f:
        f.write("Q3 revenue up 12%\n")
    yield d
    shutil.rmtree(d, ignore_errors=True)


def run(store, *args):
    env = dict(os.environ, ASSET_STORAGE_DIR=store)
    p = subprocess.run(
        [sys.executable, "-m", "assetsvc", *args],
        capture_output=True,
        text=True,
        env=env,
    )
    return p.stdout


def test_list(store):
    out = run(store, "list")
    assert "overview.txt" in out
    assert os.path.join("2024", "q3", "summary.txt") in out


def test_meta(store):
    out = run(store, "meta", "overview.txt")
    assert out.strip().isdigit()
    assert int(out.strip()) > 0
