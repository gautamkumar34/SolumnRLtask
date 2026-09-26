# Add an `export` command to assetsvc

One-off admin tool: we need to dump a stored template by name. Reuse the
helpers in `assetsvc/pathutils.py`.

## What to build

`export <path>` prints the stored asset at `<path>`, including nested paths.

## Notes

- Implement in `storage.py`, register in `cli.py`.
- `pathutils.py` has a helper to locate a stored file by name — reuse it.
- The existing tests under `tests/` must keep passing.
