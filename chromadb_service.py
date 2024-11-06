
from services.embed_service import generate_embedding

from chromadb import PersistentClient

# Check if the initialization method or arguments have changed
db_client = PersistentClient()  # Adjust the instantiation based on the updated API



def ingest_document(doc_id: str, content: str):
    embedding = generate_embedding(content)
    db_client.add(doc_id, embedding, metadata={"content": content})

def query_document(query: str, top_k: int = 5):
    embedding = generate_embedding(query)
    results = db_client.query(embedding, top_k=top_k)
    return results
