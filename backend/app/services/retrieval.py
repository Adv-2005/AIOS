from app.services.vectorstore import get_vectorstore
from app.services.bm25 import build_bm25

def retrieve_documents(
    query: str,
    k: int = 10
):
    vectorstore = get_vectorstore()

    retriever = vectorstore.as_retriever(
        search_type="mmr",
        search_kwargs={
            "k": k,
            "fetch_k": 30
        }
    )

    docs = retriever.invoke(query)

    return docs

def bm25_search(
    query: str,
    k: int = 10
):

    bm25, chunks = build_bm25()

    scores = bm25.get_scores(
        query.split()
    )

    ranked = sorted(
        zip(scores, chunks),
        key=lambda x: x[0],
        reverse=True
    )

    return [
        item[1]
        for item in ranked[:k]
    ]