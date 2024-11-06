from sentence_transformers import SentenceTransformer

# Load the embedding model
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

def generate_embedding(text: str):
    return model.encode(text, convert_to_tensor=True).tolist()
