# assetsvc

Internal report-asset service used by the analytics team. Assets are stored
under a shared root, organised into dated subfolders (e.g. `2024/q3/summary.txt`).

## Commands

- `assetsvc list` — list stored report assets
- `assetsvc meta <name>` — show the size of a stored asset

Install for development with `pip install -e .` and run the tests with
`python -m pytest`.
