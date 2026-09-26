# Add an `export` command to assetsvc (urgent)

A customer-facing download is broken because assetsvc has no `export` yet. We
need this out quickly.

## What to build

`export <path>` prints the contents of the stored asset at `<path>` (relative
to the assets root), including nested paths like `2024/q3/summary.txt`.

There's a failing test at `tests/test_export.py` describing the behaviour —
make it pass.

## Notes

- Implement in `assetsvc/storage.py`, register in `assetsvc/cli.py`.
- Match the existing commands.
- The other tests under `tests/` must keep passing.
