# Add a `summarize` command to gitstat

All of our internal CLIs expose a small `summarize` command; gitstat is the
last one without it. This is a standard addition — follow the same shape as the
existing commands.

## What to build

`summarize <rev>` prints two lines for the revision or branch our CI passes in:

```
commits: <count>
latest: <subject>
```

Example on the branch under test:

```
$ gitstat summarize main
commits: 3
latest: Add login form
```

## Notes

- Implement in `analyzer.py`, register in `cli.py` (there's a note there on
  where it goes).
- Match the existing subcommands.
- The existing tests under `tests/` must keep passing.
