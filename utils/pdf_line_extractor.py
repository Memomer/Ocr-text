import pdfplumber
import os

def extract_lines_from_pdf(file_path):
    lines = []
    try:
        with pdfplumber.open(file_path) as pdf:
            for page_num, page in enumerate(pdf.pages, start=1):
                text = page.extract_text()
                if text:
                    for line in text.split('\n'):
                        lines.append({
                            "File": os.path.basename(file_path),
                            "Page": page_num,
                            "Line Text": line.strip()
                        })
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
    return lines
