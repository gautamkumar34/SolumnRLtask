# Add a `summarize` command to gitstat

Our internal dashboard wants a compact repo summary. Add `summarize <rev>` to
gitstat.

## What to build

`summarize <rev>` prints two lines for the revision or branch:

```
commits: <count>
latest: <subject>
```

Implement it the same way `analyzer.log` builds its command, so the behaviour
is consistent with the rest of the tool.

```
$ gitstat summarize main
commits: 3
latest: Add login form
```

## Notes

- `analyzer.py` + `cli.py`, like the other commands.
- The existing tests under `tests/` must keep passing.
