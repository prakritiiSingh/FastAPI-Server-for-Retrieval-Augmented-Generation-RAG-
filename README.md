

---

# **FastAPI Server for Retrieval-Augmented Generation (RAG)**

This repository provides a FastAPI server optimized for Retrieval-Augmented Generation (RAG), enabling seamless document ingestion, storage, and retrieval. It leverages ChromaDB for efficient data storage and Sentence-Transformers for robust document embeddings.

---

## **Features**

- **Document Storage & Search**  
  Efficiently ingest and query documents in PDF, DOC, DOCX, and TXT formats using ChromaDB.
  
- **Semantic Embeddings**  
  Generates embeddings using `sentence-transformers/all-MiniLM-L6-v2`, optimized for CPU.

- **Non-blocking API**  
  FastAPI’s async capabilities allow efficient handling of concurrent requests.

---

## **Tech Stack**

- **FastAPI**: High-performance, async API framework
- **ChromaDB**: Manages and retrieves vectorized document embeddings
- **Sentence-Transformers**: Embedding generation using transformer models
- **Uvicorn**: ASGI server for deployment

---

## **Libraries & Tools**

- **FastAPI**: Framework for rapid API development
- **Uvicorn**: High-performance ASGI server for FastAPI
- **ChromaDB**: Vector database for document embeddings
- **Sentence-Transformers**: Embedding model for semantic text processing
- **Langchain**: Simplifies document ingestion and processing

---

## **Getting Started**

### **Prerequisites**

- **Python 3.8+**
- **pip** for package installation

### **Installation Steps**

1. **Clone the Repository**  
   ```bash
   [git clone https://github.com/fastapi-rag-server.git](https://github.com/prakritiiSingh/FastAPI-Server-for-Retrieval-Augmented-Generation-RAG-.git)
   cd fastapi-rag-server
   ```

2. **Install Required Packages**  
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Server**  
   ```bash
   uvicorn main:app --reload
   ```

   The server can now be accessed at: [http://127.0.0.1:8000](http://127.0.0.1:8000).

---

## **API Endpoints**

1. **`/ingest/` [POST]**  
   Uploads documents (PDF, DOC, DOCX, TXT) to the database.
   - **Request**: Multipart form with files
   - **Response**: `{ "status": "Documents uploaded successfully" }`

2. **`/query/` [GET]**  
   Searches stored documents based on a query.
   - **Parameter**: `query_text` (string) - search term
   - **Response**: `{ "results": [{ "filename": "sample1.txt", "score": 0.7214, "text": "..." }] }`

3. **`/database/` [GET]**  
   Retrieves all stored documents with metadata.
   - **Response**: `{ "documents": [{ "filename": "sample1.txt", "text": "..." }] }`

---

## **Running the Server**

To start the server, run:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

The server will be accessible at: [http://localhost:8000](http://localhost:8000).

---

## **Testing the API**

Use API clients like **Postman** or **Thunder Client** to test requests:

- **Ingest Documents**: Upload files with a POST request to `/ingest/`.
- **Query Documents**: Send a GET request to `/query/` with a `query_text` parameter.

---

## **Contributing**

We welcome contributions! Please submit a Pull Request.

For questions, contact **Prakriti** at [Prakriti14a14j@gmail.com](mailto:Prakriti14a14j@gmail.com).

---

## **License**

This project is licensed under the **MIT License**.

---

## **Acknowledgments**

Special thanks to the following resources for supporting this project:

- **FastAPI**
- **ChromaDB**
- **Sentence-Transformers**
- **Langchain**

---
