"""Path helpers retained for the admin tooling."""

import os

from .storage import STORAGE_DIR


def locate(name):
    """Return the path of a stored file by name."""
    return os.path.join(STORAGE_DIR, name)
