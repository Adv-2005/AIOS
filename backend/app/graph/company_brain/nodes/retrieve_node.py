from app.services.retrieval import retrieve_documents


def retrieve_node(state):

    docs = retrieve_documents(
        state["question"]
    )

    return {
        "documents": docs
    }