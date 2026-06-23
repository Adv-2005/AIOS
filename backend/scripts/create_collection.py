# scripts/create_collection.py

from qdrant_client import QdrantClient
from qdrant_client.models import Distance
from qdrant_client.models import VectorParams

client = QdrantClient(
    url="http://localhost:6333"
)

collections = [
    c.name
    for c in client.get_collections().collections
]

if "company_brain" not in collections:

    client.create_collection(
        collection_name="company_brain",
        vectors_config=VectorParams(
            size=3072,
            distance=Distance.COSINE
        )
    )

    print("Collection Created")

else:
    print("Already Exists")