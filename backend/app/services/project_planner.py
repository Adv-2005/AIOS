from sqlalchemy.orm import Session

from app.services.llm import get_project_planner_llm
from app.schemas.project_plan import ProjectPlan
from app.models.project import Project
from app.models.task import Task
from app.models.task_dependencies import TaskDependency

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
- task_id
- title
- detailed description
- priority (Low, Medium, High)
- estimated effort in hours
- depends_on
- suggested_role

Choose ONE suggested_role from:

- Backend Developer
- Frontend Developer
- Full Stack Developer
- AI/ML Engineer
- DevOps Engineer
- QA Engineer
- UI/UX Designer
- Product Manager

Rules:

- task_id must start from 1.
- task_ids must be unique.
- depends_on must contain task_ids.
- Tasks with no dependency should return [].
- A task may depend on multiple earlier tasks.
- Never depend on future tasks.

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
        status="planned",
)

    db.add(project)
    db.flush()  # Ensure the project ID is generated

    task_id_mapping = {}

    for task in plan.tasks:

        db_task = Task(
            project_id=project.id,
            title=task.title,
            description=task.description,
            priority=task.priority,
            estimated_hours=task.estimated_hours,
            suggested_role=task.suggested_role,
            status="todo"
        )

        db.add(db_task)
        db.flush()  # Ensure the task ID is generated
        task_id_mapping[task.task_id] = db_task.id
    for task in plan.tasks:

        current_task_id = task_id_mapping[task.task_id]

        for dependency in task.depends_on:
            if dependency not in task_id_mapping:
                raise ValueError(
                    f"Invalid dependency: Task {task.task_id} depends on unknown task {dependency}"
                )
            db_dependency = TaskDependency(
                task_id=current_task_id,
                depends_on_task_id=task_id_mapping[dependency]
            )

            db.add(db_dependency)
    try:
        db.commit()
        db.refresh(project)  # Refresh to get the updated project with ID
        return project.id
    except Exception:
        db.rollback()
        raise 
