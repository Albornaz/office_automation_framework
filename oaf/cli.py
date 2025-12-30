import argparse
from oaf.security.access import check_permission
from examples.daily_financial_report import run

def main():
    parser = argparse.ArgumentParser("oaf")
    parser.add_argument("--role", required=True, help="User role")

    subparsers = parser.add_subparsers(dest="command")

    run_cmd = subparsers.add_parser("run")
    run_cmd.add_argument("job")

    args = parser.parse_args()

    if args.command == "run" and args.job == "report":
        check_permission(args.role, "run_report")
        run()
    else:
        parser.print_help()

