"""Command-line entrypoint for assetsvc."""

import argparse

from . import storage


def main(argv=None):
    parser = argparse.ArgumentParser(
        prog="assetsvc", description="Internal report asset service"
    )
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("list", help="List stored report assets")
    p_meta = sub.add_parser("meta", help="Show the size of a stored asset")
    p_meta.add_argument("name")
    # An `export <path>` subcommand is added here — see instruction.md.

    args = parser.parse_args(argv)

    if args.command == "list":
        print("\n".join(storage.list_assets()))
    elif args.command == "meta":
        print(storage.asset_size(args.name))
    else:  # pragma: no cover - argparse rejects unknown commands first
        parser.error(f"unknown command: {args.command}")


if __name__ == "__main__":
    main()
