# app/graph/company_brain/state.py

from typing import TypedDict
from langchain_core.documents import Document


class BrainState(TypedDict):
    question: str
    rewritten_query: str
    documents: list[Document]
    answer: str
    sources: list[str]