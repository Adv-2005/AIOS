# app/services/vectorstore.py

from qdrant_client import QdrantClient

from langchain_qdrant import QdrantVectorStore

from app.core.config import settings
from app.services.embeddings import get_embeddings
from qdrant_client.models import (
    Distance,
    VectorParams
)


def get_vectorstore():

    client = QdrantClient(
        url=settings.QDRANT_URL
    )
    collections = [
        c.name
        for c in client.get_collections().collections
    ]
    if settings.COLLECTION_NAME not in collections:

        client.create_collection(
            collection_name=settings.COLLECTION_NAME,
            vectors_config=VectorParams(
                size=3072,  
                distance=Distance.COSINE
            )
        )

        print("Collection Created")

    return QdrantVectorStore(
        client=client,
        collection_name=settings.COLLECTION_NAME,
        embedding=get_embeddings()
    )