## Approach Explanation

The goal is to extract and rank relevant sections from a set of PDFs based on a persona and a specific job-to-be-done.

### Step 1: PDF Text Extraction
Using `pdfplumber` and `PyMuPDF`, each page of the PDFs is parsed. Sections are detected using heuristics like font size, layout position, and paragraph grouping.

### Step 2: Embedding Persona-Job Intent
We use `sentence-transformers` with the `all-MiniLM-L6-v2` model (80MB) to convert the persona+job into an embedding vector.

### Step 3: Matching and Scoring
Each section's text is embedded and compared using cosine similarity to the persona-job vector. Top sections are ranked.

### Step 4: Sub-section Refinement
Top-ranked sections are further broken down to identify key paragraphs most relevant to the job.

### Compliance
- ✅ Model size < 1GB
- ✅ No internet or API
- ✅ Docker-compatible and CPU-only
- ✅ Runs within 60 seconds for 5 documents

The entire solution runs fully offline and is containerized for robust testing.