from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import get_db

from app.schemas.kpi import DashboardResponse
from app.services.kpi import get_dashboard


router = APIRouter(
    prefix="/kpi",
    tags=["KPI Dashboard"]
)


@router.get(
    "/dashboard",
    response_model=DashboardResponse
)
def dashboard(
    db: Session = Depends(get_db)
):

    return get_dashboard(db)