"""Spec test for the new `export` command (currently failing)."""

import os
import shutil
import subprocess
import sys
import tempfile

import pytest


@pytest.fixture
def store():
    d = tempfile.mkdtemp()
    os.makedirs(os.path.join(d, "2024", "q3"))
    with open(os.path.join(d, "2024", "q3", "summary.txt"), "w") as f:
        f.write("Q3 revenue up 12%\n")
    yield d
    shutil.rmtree(d, ignore_errors=True)


def run(store, *args):
    env = dict(os.environ, ASSET_STORAGE_DIR=store)
    return subprocess.run(
        [sys.executable, "-m", "assetsvc", *args],
        capture_output=True, text=True, env=env,
    ).stdout


# export should locate the file like the other commands — e.g. asset_size(name)
# uses storage.asset_path(name), i.e.  os.path.join(STORAGE_DIR, name)
def test_export_nested(store):
    out = run(store, "export", "2024/q3/summary.txt")
    assert "Q3 revenue up 12%" in out
