# Add a `summarize` command to gitstat

`gitstat` is our internal repository-analysis CLI. It already ships three
subcommands — `branches`, `authors`, and `activity` — implemented in
`gitstat/analyzer.py` and wired up in `gitstat/cli.py`. We need one more.

## What to build

Add a `summarize <rev>` subcommand that, for the given revision or branch name,
prints exactly two lines:

```
commits: <number of commits reachable from rev>
latest: <subject line of the most recent commit on rev>
```

For example, in a repo whose newest commit on `main` is "Add login form" and
which has three commits in total:

```
$ gitstat summarize main
commits: 3
latest: Add login form
```

## Notes

- Implement the logic in `gitstat/analyzer.py` and register the subcommand in
  `gitstat/cli.py`, next to the existing ones.
- Keep it consistent with how the other subcommands are written.
- The existing tests under `tests/` must keep passing — run `python -m pytest`
  before you finish.
- `summarize` should accept any revision or branch name (for example `main` or
  a commit SHA).
