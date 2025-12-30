from oaf.data.loader import load_csv
from oaf.data.processor import process_dataframe
from oaf.reports.html import generate_html_report
from oaf.reports.pdf import html_to_pdf
from oaf.files.manager import ensure_dir

def run():
    ensure_dir("reports")

    df = load_csv("data/finance.csv")
    df = process_dataframe(df)

    html_path = "reports/financial_report.html"
    pdf_path = "reports/financial_report.pdf"

    generate_html_report(
        df,
        "oaf/reports/templates/financial_report_template.html",
        html_path
    )

    html_to_pdf(html_path, pdf_path)

    print("HTML and PDF reports generated.")
