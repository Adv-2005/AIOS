from fastapi import APIRouter

from app.schemas.brain import BrainRequest

from app.graph.company_brain.graph import (
    build_company_brain
)

router = APIRouter()

graph = build_company_brain()

@router.post("/chat")
def company_brain_chat(
    request: BrainRequest
):

    result = graph.invoke(
        {
            "question": request.question
        }
    )

    return {
        "answer": result["answer"],
        "sources": result["sources"]
    }