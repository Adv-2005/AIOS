# app/api/routes/strategy.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import get_db

from app.graph.strategy.graph import graph

from app.schemas.strategy import (
    MondaySessionReport,
    MondaySessionRequest,
)

router = APIRouter(
    tags=["Strategy"],
)


@router.post(
    "/monday-session",
    response_model=MondaySessionReport,
)
def generate_monday_session(
    request: MondaySessionRequest,
    db: Session = Depends(get_db),
):
    """
    Generate the weekly Monday leadership session report.

    The report combines:
    - Project status
    - Task progress
    - Operational risks
    - High priority work
    - Industry trends from the web
    """

    result = graph.invoke(
        {},
        config={
            "configurable": {
                "db": db,
            }
        },
    )

    return result["monday_session"]