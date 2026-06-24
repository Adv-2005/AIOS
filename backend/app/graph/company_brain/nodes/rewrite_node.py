from app.services.query_rewrite import (
    rewrite_query
)


def rewrite_node(state):

    rewritten = rewrite_query(
        state["question"]
    )

    return {
        "rewritten_query": rewritten
    }