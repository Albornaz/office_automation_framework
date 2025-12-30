import argparse
from oaf.data.processor import process_data
from oaf.reports.html_report import generate_html_report

def run_cli():
    parser = argparse.ArgumentParser(description="Office Automation Framework")
    parser.add_argument("--process", help="Process data file")
    parser.add_argument("--report", action="store_true", help="Generate report")

    args = parser.parse_args()

    if args.process:
        process_data(args.process)

    if args.report:
        generate_html_report()
