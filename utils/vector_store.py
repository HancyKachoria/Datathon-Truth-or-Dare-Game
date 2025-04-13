import chromadb
from chromadb.config import Settings
import numpy as np
from typing import List, Dict, Any
import os

# Initialize ChromaDB client
client = None
collection = None


def init_vector_store():
    """
    Initialize the ChromaDB vector store.
    """
    global client, collection

    # Create a persistent ChromaDB instance
    client = chromadb.PersistentClient(
        path="chroma_db",
        settings=Settings(
            anonymized_telemetry=False
        )
    )

    # Create or get the collection
    collection = client.get_or_create_collection(
        name="document_chunks",
        metadata={"hnsw:space": "cosine"}
    )


def store_chunks(chunks: List[str], embeddings: List[List[float]], metadata: List[Dict[str, Any]] = None):
    """
    Store document chunks and their embeddings in the vector store.

    Args:
        chunks: List of text chunks
        embeddings: List of embedding vectors
        metadata: Optional list of metadata dictionaries
    """
    if metadata is None:
        metadata = [{} for _ in chunks]

    # Convert embeddings to list of lists for ChromaDB
    embeddings_list = [list(embedding) for embedding in embeddings]

    # Generate IDs for the chunks
    ids = [f"chunk_{i}" for i in range(len(chunks))]

    # Add to collection
    collection.add(
        documents=chunks,
        embeddings=embeddings_list,
        metadatas=metadata,
        ids=ids
    )


def search_similar_chunks(query_embedding: List[float], n_results: int = 5) -> List[Dict[str, Any]]:
    """
    Search for similar chunks based on a query embedding.

    Args:
        query_embedding: The embedding vector to search with
        n_results: Number of results to return

    Returns:
        List of dictionaries containing the similar chunks and their metadata
    """
    results = collection.query(
        query_embeddings=[list(query_embedding)],
        n_results=n_results
    )

    # Format results
    similar_chunks = []
    for i in range(len(results['documents'][0])):
        chunk = {
            'text': results['documents'][0][i],
            'metadata': results['metadatas'][0][i],
            'distance': results['distances'][0][i]
        }
        similar_chunks.append(chunk)

    return similar_chunks
