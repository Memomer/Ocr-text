import os
from utils.pdf_line_extractor import extract_lines_from_pdf
from utils.excel_writer import write_lines_to_excel

INPUT_DIR = "samples"
OUTPUT_FILE = "output/invoice_lines.xlsx"

if __name__ == "__main__":
    all_lines = []
    for file in os.listdir(INPUT_DIR):
        if file.lower().endswith(".pdf"):
            full_path = os.path.join(INPUT_DIR, file)
            print(f"📄 Processing {file}...")
            lines = extract_lines_from_pdf(full_path)
            all_lines.extend(lines)

    if all_lines:
        write_lines_to_excel(all_lines, OUTPUT_FILE)
        print(f"✅ Done! Lines saved to {OUTPUT_FILE}")
    else:
        print("❌ No lines extracted.")
