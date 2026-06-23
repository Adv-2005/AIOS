# app/services/vectorstore.py

from qdrant_client import QdrantClient

from langchain_qdrant import QdrantVectorStore

from app.core.config import settings
from app.services.embeddings import get_embeddings


def get_vectorstore():

    client = QdrantClient(
        url=settings.QDRANT_URL
    )

    return QdrantVectorStore(
        client=client,
        collection_name=settings.COLLECTION_NAME,
        embedding=get_embeddings()
    )