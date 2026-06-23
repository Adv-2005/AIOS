from app.services.retrieval import retrieve_documents


def retrieve_node(state):

    docs = retrieve_documents(
        state["question"]
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