import argparse
import pathlib

def init(args):
    print(f"init: {args}")

def run(args):
    print(f"run: {args}")

def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(required=True, dest="action")
    init_parser = subparsers.add_parser("init")
    init_parser.set_defaults(func=init)
    init_parser.add_argument(
        "-b",
        "--base",
        type=pathlib.Path,
        default=pathlib.Path("."),
    )
    run_parser = subparsers.add_parser("run")
    run_parser.set_defaults(func=run)
    run_parser.add_argument(
        "-b",
        "--base",
        type=pathlib.Path,
        default=pathlib.Path("."),
    )
    run_parser.add_argument("files", nargs="*", type=pathlib.Path, metavar="FILE")
    args = parser.parse_args()
    args.func(args)
    parser.print_help()

if __name__ == "__main__":
    main()
