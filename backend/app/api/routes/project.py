from app.schemas.project_plan import ProjectRequest
from app.graph.project.graph import build_project_graph
from fastapi import APIRouter
from app.services.project_planner import save_project_plan
from fastapi import Depends
from sqlalchemy.orm import Session
from fastapi import UploadFile
from fastapi import File
from pathlib import Path

from app.services.project_planner import save_project_plan
from app.services.project_ingestion import extract_requirement

from app.api.deps import get_db

router = APIRouter()

graph = build_project_graph()

@router.post("/generate")
def generate_project(
    request: ProjectRequest,
    db: Session = Depends(get_db)
):

    result = graph.invoke(
        {
            "requirement": request.requirement
        }
    )

    plan= result["project_plan"]
    project_id = save_project_plan(plan, db)
    return {
    "project_id": project_id,
    "project_name": plan.project_name,
    "tasks_created": len(plan.tasks),
    "milestones_created": len(plan.milestones),
    "project_plan": plan
}

@router.post("/upload")
async def upload_project_requirement(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    Path("uploads").mkdir(exist_ok=True)

    file_path = f"uploads/{file.filename}"

    with open(file_path, "wb") as f:
        f.write(await file.read())

    requirement = extract_requirement(file_path)

    result = graph.invoke(
        {
            "requirement": requirement
        }
    )

    plan = result["project_plan"]

    project_id = save_project_plan(
        plan,
        db
    )

    return {
        "message": "Project generated successfully",
        "project_id": project_id,
        "project_plan": plan
    }
