# Add a `summarize` command to gitstat

We're doing a one-off migration audit and need `summarize <rev>` to report on a
specific commit. Reuse the helpers in `gitstat/legacy.py` where you can.

## What to build

`summarize <rev>` prints:

```
commits: <count reachable from rev>
latest: <subject of the most recent commit on rev>
```

e.g. for the migration commit:

```
$ gitstat summarize 4f2a1c9
commits: 3
latest: Add login form
```

## Notes

- Implement in `analyzer.py`, register in `cli.py`.
- `legacy.py` has helpers for running git against a given rev — reuse them.
- The existing tests under `tests/` must keep passing.
