from sentence_transformers import SentenceTransformer

# This will download and save the model locally
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
model.save('./all-MiniLM-L6-v2')