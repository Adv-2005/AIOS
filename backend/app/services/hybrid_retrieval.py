from app.services.retrieval import retrieve_documents
from app.services.retrieval import bm25_search

from langchain_core.documents import Document

def hybrid_search(
    query: str,
    k: int = 20
):

    vector_docs = retrieve_documents(
        query,
        k=10
    )

    bm25_docs = bm25_search(
        query,
        k=10
    )

    merged = []

    seen = set()

    for doc in vector_docs:

        text = doc.page_content

        if text not in seen:
            seen.add(text)
            merged.append(doc)

    for chunk in bm25_docs:

        text = chunk.content

        if text not in seen:

            merged.append(
                Document(
                    page_content=text,
                    metadata={}
                )
            )

            seen.add(text)

    return merged