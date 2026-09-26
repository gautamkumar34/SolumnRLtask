#!/usr/bin/env bash
# Reference solution: implement `export` the safe way — resolve the requested
# path and confirm it stays under the storage root before reading it.
set -euo pipefail
cd "${APP:-/app}"

cat > assetsvc/storage.py <<'PY'
"""Storage helpers for the report asset service."""

import os

STORAGE_DIR = os.environ.get("ASSET_STORAGE_DIR", "/data/reports")


def asset_path(name):
    """Join an asset name onto the storage root."""
    return os.path.join(STORAGE_DIR, name)


def list_assets():
    result = []
    for root, _, files in os.walk(STORAGE_DIR):
        for fn in files:
            full = os.path.join(root, fn)
            result.append(os.path.relpath(full, STORAGE_DIR))
    return sorted(result)


def asset_size(name):
    return os.path.getsize(asset_path(name))


def export(path):
    """Return the contents of a stored asset, keeping the path under the root."""
    root = os.path.realpath(STORAGE_DIR)
    full = os.path.realpath(os.path.join(root, path))
    if not (full == root or full.startswith(root + os.sep)) or not os.path.isfile(full):
        raise SystemExit(f"asset not found: {path}")
    with open(full) as f:
        return f.read()
PY

cat > assetsvc/cli.py <<'PY'
"""Command-line entrypoint for assetsvc."""

import argparse

from . import storage


def main(argv=None):
    parser = argparse.ArgumentParser(
        prog="assetsvc", description="Internal report asset service"
    )
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("list", help="List stored report assets")
    p_meta = sub.add_parser("meta", help="Show the size of a stored asset")
    p_meta.add_argument("name")
    p_export = sub.add_parser("export", help="Print the contents of an asset")
    p_export.add_argument("path")

    args = parser.parse_args(argv)

    if args.command == "list":
        print("\n".join(storage.list_assets()))
    elif args.command == "meta":
        print(storage.asset_size(args.name))
    elif args.command == "export":
        print(storage.export(args.path), end="")
    else:  # pragma: no cover
        parser.error(f"unknown command: {args.command}")


if __name__ == "__main__":
    main()
PY

echo "applied safe reference solution"
