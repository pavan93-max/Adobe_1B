import os
import json
import time
from datetime import datetime, timezone
from extractor import extract_sections
from ranker import rank_sections, refine_sections

input_dir = "input"
output_dir = "output"

def load_persona_job():
    for file in os.listdir(input_dir):
        if file.endswith(".json"):
            with open(os.path.join(input_dir, file), "r") as f:
                return json.load(f)
    return None

def main():
    start = time.time()
    metadata = load_persona_job()
    if not metadata:
        raise Exception("Persona JSON missing in input folder.")
    persona = metadata["persona"]
    job = metadata["job"]

    all_sections = []
    for file in os.listdir(input_dir):
        if file.endswith(".pdf"):
            filepath = os.path.join(input_dir, file)
            sections = extract_sections(filepath)
            for s in sections:
                s["document"] = file
            all_sections.extend(sections)

    ranked = rank_sections(all_sections, persona, job)
    refined = refine_sections(ranked[:5], persona, job)

    output = {
        "metadata": {
            "input_documents": [f for f in os.listdir(input_dir) if f.endswith(".pdf")],
            "persona": persona,
            "job_to_be_done": job,
            "processing_timestamp": datetime.now(timezone.utc).isoformat()

        },
        "extracted_sections": [
            {
                "document": s["document"],
                "section_title": s["section_title"],
                "importance_rank": s["importance_rank"],
                "page_number": s.get("page_number", s.get("page", None))
            }
            for s in ranked[:5]  # Only top 5
        ],
        "subsection_analysis": [
            {
                "document": s["document"],
                "refined_text": s["refined_text"],
                "page_number": s.get("page_number", s.get("page", None))
            }
            for s in refined[:5]  # Only top 5
        ]
    }

    with open(os.path.join(output_dir, "output.json"), "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    main()