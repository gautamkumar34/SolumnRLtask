# Add an `export` command to assetsvc

The analytics dashboard needs to fetch report contents. Add `export <path>`.

## What to build

`export <path>` prints the stored asset at `<path>`, including nested paths
like `2024/q3/summary.txt`.

Locate the file the same way `meta` does (via `asset_path`), so behaviour is
consistent with the rest of the service.

## Notes

- Implement in `storage.py`, register in `cli.py`.
- The existing tests under `tests/` must keep passing.
