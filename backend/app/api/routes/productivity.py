from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.graph.productivity.graph import graph
from app.schemas.productivity import (
    ProductivityRequest,
    ProductivityPlan,
)

router = APIRouter(
    prefix="/productivity",
    tags=["Productivity Agent"],
)


@router.post(
    "/generate",
    response_model=ProductivityPlan,
)
def generate_productivity(
    request: ProductivityRequest,
    db: Session = Depends(get_db),
):
    result = graph.invoke(
        {
            "role": request.role,
        },
        config={
            "configurable": {
                "db": db
            }
        }
    )

    return result["productivity_plan"]