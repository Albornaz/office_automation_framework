from weasyprint import HTML

class PDFReport:
    @staticmethod
    def from_html(html: str, output_path: str):
        HTML(string=html).write_pdf(output_path)
