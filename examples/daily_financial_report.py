from oaf.data.loader import load_csv
from oaf.data.processor import process_dataframe
from oaf.data.exporter import export_csv
from oaf.reports.html import generate_html_report
from oaf.files.manager import ensure_dir

def run():
    ensure_dir("reports")

    df = load_csv("data/finance.csv")
    df = process_dataframe(df)

    export_csv(df, "reports/summary.csv")

    generate_html_report(
        df,
        "oaf/reports/templates/financial_report_template.html",
        "reports/financial_report.html"
    )

if __name__ == "__main__":
    run()
