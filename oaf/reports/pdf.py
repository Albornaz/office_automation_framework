from pathlib import Path
from weasyprint import HTML

def html_to_pdf(html_path: str, pdf_path: str):
    HTML(html_path).write_pdf(pdf_path)

