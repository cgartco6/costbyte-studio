from backend.services.document_creator import generate_pdf_from_html
from backend.services.zip_creator import create_zip_from_files

html = "<h1>VAT Tracker</h1><p>12-month turnover: R0</p>"
pdf_bytes = generate_pdf_from_html(html)
with open("generated/vat_tracker.pdf", "wb") as f:
    f.write(pdf_bytes)

zip_buffer = create_zip_from_files(["generated/vat_tracker.pdf"])
with open("generated/bundle.zip", "wb") as f:
    f.write(zip_buffer.getvalue())

print("✅ PDF & ZIP generated")
