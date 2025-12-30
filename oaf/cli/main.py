import argparse
from datetime import date

from oaf.reports.html import HTMLReport
from oaf.reports.pdf import PDFReport
from oaf.security.access import AccessControl


def generate_report(args):
    AccessControl.validate(args.access)

    context = {
        "report_title": args.title,
        "report_date": args.date,
        "department": args.department,
        "author": args.author,
        "company_name": args.company,
        "access_level": args.access,

        "kpi": {
            "Revenue": "1 200 0 €",
            "Profit": "400 00 €"
        },

        "tables": [],
        "chart": {
            "title": "Revenue",
            "labels": ["Mon", "Tue", "Wed"],
            "values": [200, 300, 400]
        }
    }

    html = HTMLReport(args.templates).render(args.template, context)
    PDFReport.from_html(html, args.output)

    print(f"✅ Report created: {args.output}")


def main():
    parser = argparse.ArgumentParser(
        prog="oaf",
        description="Office Automation Framework CLI"
    )

    subparsers = parser.add_subparsers(dest="command")

    # report
    report_parser = subparsers.add_parser("report", help="Working with reports")
    report_sub = report_parser.add_subparsers(dest="action")

    # report generate
    gen = report_sub.add_parser("generate", help="Generate a report")

    gen.add_argument("--title", default="Financial report")
    gen.add_argument("--date", default=str(date.today()))
    gen.add_argument("--department", default="Finance")
    gen.add_argument("--author", default="OAF")
    gen.add_argument("--company", default="Speace")

    gen.add_argument(
        "--access",
        choices=["public", "internal", "confidential"],
        default="internal"
    )

    gen.add_argument(
        "--template",
        default="financial_report_template.html"
    )

    gen.add_argument(
        "--templates",
        default="oaf/reports/templates",
        help="Path to templates"
    )

    gen.add_argument(
        "--output",
        default="report.pdf",
        help="Output PDF file"
    )

    gen.set_defaults(func=generate_report)

    args = parser.parse_args()

    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
