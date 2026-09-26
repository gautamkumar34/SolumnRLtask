"""Command-line entrypoint for gitstat."""

import argparse

from . import analyzer


def main(argv=None):
    parser = argparse.ArgumentParser(
        prog="gitstat", description="Internal repository analysis CLI"
    )
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("branches", help="List the repo's branches")
    sub.add_parser("authors", help="List distinct commit authors")
    sub.add_parser("activity", help="Show commit activity by day")
    p_log = sub.add_parser("log", help="Show recent commits on a revision")
    p_log.add_argument("rev")
    # Add `summarize` here; build its git command with run_cmd(f"...") like log().
    # A `summarize <rev>` subcommand is added here — see instruction.md.

    args = parser.parse_args(argv)

    if args.command == "branches":
        print("\n".join(analyzer.list_branches()))
    elif args.command == "authors":
        print("\n".join(analyzer.list_authors()))
    elif args.command == "activity":
        print("\n".join(analyzer.activity()))
    elif args.command == "log":
        print("\n".join(analyzer.log(args.rev)))
    else:  # pragma: no cover - argparse rejects unknown commands first
        parser.error(f"unknown command: {args.command}")


if __name__ == "__main__":
    main()
