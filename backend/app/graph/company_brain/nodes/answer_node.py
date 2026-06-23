from app.services.llm import get_llm

llm = get_llm()


def answer_node(state):

    context = "\n\n".join(
        doc.page_content
        for doc in state["documents"]
    )

    prompt = f"""
You are the AI COO Company Brain.

Answer ONLY using the provided context.

If the answer cannot be found in the context,
say:

"I could not find that information in the company knowledge base."

Context:
{context}

Question:
{state["question"]}
"""

    response = llm.invoke(prompt)

    return {
        "answer": response.content
    }