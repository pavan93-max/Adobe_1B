# Adobe Hackathon Round 1B Solution

## 🔧 How to Build and Run

```bash
docker build --platform linux/amd64 -t mysolution:offlinegenius .
docker run --rm -v $(pwd)/input:/app/input -v $(pwd)/output:/app/output --network none mysolution:offlinegenius
```

Ensure the `input/` folder contains the PDF files and `persona_input.json`.

## 📁 Folder Structure

- `main.py`: Main entrypoint for execution
- `extractor.py`: Handles PDF reading and sectioning
- `ranker.py`: Handles embeddings and scoring
- `utils.py`: Helper functions
- `approach_explanation.md`: Approach and logic behind the solution