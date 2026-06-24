from app.services.llm import get_llm

llm = get_llm()


def rewrite_query(question: str) -> str:

    prompt = f"""
You are a search query optimizer.

Rewrite the question into the best possible search query
for retrieving company documents.

Question:
{question}

Only return the rewritten query.
"""

    response = llm.invoke(prompt)

    return response.content.strip()