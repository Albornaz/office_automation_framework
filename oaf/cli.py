import argparse
from examples.daily_financial_report import run

def main():
    parser = argparse.ArgumentParser(
        prog="oaf",
        description="Office Automation Framework CLI"
    )

    subparsers = parser.add_subparsers(dest="command")

    run_cmd = subparsers.add_parser("run", help="Run automation jobs")
    run_cmd.add_argument("job", help="Job name (e.g. report)")

    args = parser.parse_args()

    if args.command == "run" and args.job == "report":
        run()
    else:
        parser.print_help()
