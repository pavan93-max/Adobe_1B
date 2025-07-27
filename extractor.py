import pdfplumber

def extract_sections(filepath):
    sections = []
    with pdfplumber.open(filepath) as pdf:
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if not text:
                continue
            lines = text.split("\n")
            for line in lines:
                if len(line.strip()) > 50:
                    sections.append({
                        "page": i+1,
                        "section_title": line.strip(),
                        "section_text": line.strip()
                    })
    return sections