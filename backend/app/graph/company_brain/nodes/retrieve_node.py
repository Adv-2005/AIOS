
from app.services.hybrid_retrieval import hybrid_search
from app.services.reranker import rerank_documents


def retrieve_node(state):

    # future:
    # filter docs based on visibility

    docs = hybrid_search(
        state["rewritten_query"],
    )
    docs = rerank_documents(
        state["question"],
        docs,
        top_k=5
    )
    sources = list(
        set(
            doc.metadata.get("filename", "Unknown")
            for doc in docs
        )
    )

    return {
        "documents": docs,
        "sources": sources
    }