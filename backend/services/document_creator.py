from weasyprint import HTML
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import io
import os

def generate_pdf_from_html(html_content: str, output_path: str = None):
    """Primary: WeasyPrint for rich HTML → PDF"""
    try:
        html = HTML(string=html_content)
        pdf_bytes = html.write_pdf()
        if output_path:
            with open(output_path, "wb") as f:
                f.write(pdf_bytes)
        return pdf_bytes
    except Exception as e:
        print(f"WeasyPrint failed: {e} → fallback to ReportLab")

        # Fallback: simple text PDF
        buffer = io.BytesIO()
        c = canvas.Canvas(buffer, pagesize=A4)
        c.drawString(100, 750, "CostByte Generated Document (fallback mode)")
        # Add more text lines...
        c.save()
        buffer.seek(0)
        return buffer.read()

def generate_simple_doc(content: str, format: str = "pdf"):
    """Quick text → PDF"""
    if format == "pdf":
        return generate_pdf_from_html(f"<pre>{content}</pre>")
    # Future: markdown → HTML → PDF
