from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("models/all-MiniLM-L6-v2")

def rank_sections(sections, persona, job):
    combined_query = persona + ". " + job
    query_emb = model.encode(combined_query)

    for section in sections:
        sec_text = section["section_text"]
        sec_emb = model.encode(sec_text)
        section["similarity"] = float(cosine_similarity([sec_emb], [query_emb])[0][0])

    sorted_sections = sorted(sections, key=lambda x: x["similarity"], reverse=True)
    for i, sec in enumerate(sorted_sections):
        sec["importance_rank"] = i + 1
    return sorted_sections

def refine_sections(top_sections, persona, job):
    refined = []
    query_emb = model.encode(persona + ". " + job)
    for section in top_sections:
        chunks = section["section_text"].split(". ")
        for chunk in chunks:
            if len(chunk) < 20:
                continue
            emb = model.encode(chunk)
            sim = float(cosine_similarity([emb], [query_emb])[0][0])
            if sim > 0.5:
                refined.append({
                    "document": section["document"],
                    "refined_text": chunk.strip(),
                    "page": section["page"]
                })
    return refined