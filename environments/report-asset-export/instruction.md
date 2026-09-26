# Add an `export` command to assetsvc

`assetsvc` is our internal report-asset service. Analysts store generated
report files under a shared assets root, organised into dated subfolders
(for example `2024/q3/summary.txt`). It already ships `list` and `meta`,
implemented in `assetsvc/storage.py` and wired up in `assetsvc/cli.py`. We need
one more.

## What to build

Add an `export <path>` subcommand that prints the contents of the stored asset
at `<path>` (relative to the assets root) to stdout.

```
$ assetsvc export 2024/q3/summary.txt
Q3 revenue up 12%
```

## Notes

- Implement the logic in `assetsvc/storage.py` and register the subcommand in
  `assetsvc/cli.py`, next to the existing ones.
- Assets are organised in dated subfolders, so a nested path like
  `2024/q3/summary.txt` must work.
- Keep it consistent with how the existing commands look up assets.
- The existing tests under `tests/` must keep passing — run `python -m pytest`
  before you finish.
- `export` should accept any asset path, including nested ones like
  `2024/q3/summary.txt`.
