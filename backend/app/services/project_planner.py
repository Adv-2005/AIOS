from sqlalchemy.orm import Session

from app.services.llm import get_project_planner_llm
from app.schemas.project_plan import ProjectPlan
from app.models.project import Project
from app.models.task import Task

def generate_project_plan(requirement: str):
    llm = get_project_planner_llm()
    structured_llm = llm.with_structured_output(
        ProjectPlan
    )

    prompt = f"""
You are an experienced senior Technical project manager.

Requirement:

{requirement}

Generate a software project plan:

- Project name
- Executive summary
- 3–8 milestones in chronological order
- 10–20 implementation tasks
- Technical risks and mitigation strategies
- Suggested project duration in weeks
- Recommended team size

For each task provide:

- title
- detailed description
- priority (Low, Medium, High)
- estimated effort in hours


Return complete structured output.
"""

    return structured_llm.invoke(prompt)

def save_project_plan(
    plan: ProjectPlan,
    db: Session
):
    project = Project(
        name=plan.project_name,
        description=plan.summary,
        status="planned"
)

    db.add(project)
    db.flush()  # Ensure the project ID is generated

    for task in plan.tasks:

        db_task = Task(
            project_id=project.id,
            title=task.title,
            description=task.description,
            priority=task.priority,
            status="todo"
        )

        db.add(db_task)
    try:
        db.commit()
        db.refresh(project)  # Refresh to get the updated project with ID
        return project.id
    except Exception:
        db.rollback()
        raise 
