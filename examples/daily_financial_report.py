from oaf.reports.html import HTMLReport
from oaf.reports.pdf import PDFReport

context = {
    "report_title": "Daily financial report",
    "report_date": "2025-12-26",
    "department": "Finance",
    "author": "OAF",
    "company_name": "Speace",
    "access_level": "internal",
    "kpi": {
        "Выручка": "1 200 0 €",
        "Прибыль": "400 00 €"
    },
    "tables": [],
    "chart": {
        "title": "Revenue",
        "labels": ["Mon", "Tue", "Wed"],
        "values": [200, 300, 400]
    }
}

html = HTMLReport("oaf/reports/templates") \
    .render("financial_report_template.html", context)

PDFReport.from_html(html, "daily_report.pdf")
