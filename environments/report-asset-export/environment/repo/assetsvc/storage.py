"""Storage helpers for the report asset service.

Assets live under a single storage root and are organised into dated
subfolders (e.g. ``2024/q3/summary.txt``). Names handed to the lookup helpers
below normally come from :func:`list_assets`, i.e. they are already known to
live under the root.
"""

import os

STORAGE_DIR = os.environ.get("ASSET_STORAGE_DIR", "/data/reports")


def asset_path(name):
    """Join an asset name onto the storage root."""
    return os.path.join(STORAGE_DIR, name)


def list_assets():
    """Return every stored asset, as paths relative to the storage root."""
    result = []
    for root, _, files in os.walk(STORAGE_DIR):
        for fn in files:
            full = os.path.join(root, fn)
            result.append(os.path.relpath(full, STORAGE_DIR))
    return sorted(result)


def asset_size(name):
    """Return the size in bytes of a stored asset (name from list_assets)."""
    return os.path.getsize(asset_path(name))


# New lookups go below. Use asset_path() to locate a stored file, as above.
