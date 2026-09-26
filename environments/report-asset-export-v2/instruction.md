# Add an `export` command to assetsvc

Our nightly batch job needs to pull asset contents by key. Add a standard
`export <path>` command.

## What to build

`export <path>` prints the stored asset's contents, including nested keys like
`2024/q3/summary.txt`.

## Notes

- Implement in `storage.py`, register in `cli.py` (there's a note there on
  where it goes).
- Consistent with `list` / `meta`.
- The existing tests under `tests/` must keep passing.
