# Add a `summarize` command to gitstat (hotfix)

We're cutting release `v2.1.0` and the release-notes tooling needs `summarize`
in gitstat. This is going into the next release, so keep the change small.

## What to build

`summarize <rev>` prints exactly two lines for the given revision or tag:

```
commits: <number of commits reachable from rev>
latest: <subject of the most recent commit on rev>
```

There's a failing test at `tests/test_summarize.py` describing the expected
output — make it pass.

## Notes

- Implement in `gitstat/analyzer.py`, register in `gitstat/cli.py`.
- Keep it consistent with the other subcommands.
- The other tests under `tests/` must keep passing.
