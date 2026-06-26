from sqlalchemy.orm import Session

from app.models.task import Task
from app.models.task_dependencies import TaskDependency
from app.schemas.productivity import ProductivityPlan
from app.services.llm import get_project_planner_llm
from app.graph.productivity.prompts import PRODUCTIVITY_PROMPT

llm = get_project_planner_llm().with_structured_output(ProductivityPlan)

PRIORITY_ORDER = {
    "High": 3,
    "Medium": 2,
    "Low": 1,
}


def get_tasks_for_role(
    role: str,
    db: Session,
) -> list[Task]:
    """
    Returns all executable (unblocked) tasks for a given role.

    A task is executable if:
    - suggested_role matches
    - task is not completed
    - all dependency tasks are completed
    """

    tasks = (
        db.query(Task)
        .filter(
            Task.suggested_role == role,
            Task.status != "completed"
        )
        .all()
    )

    available_tasks = []

    for task in tasks:

        dependencies = (
            db.query(TaskDependency)
            .filter(TaskDependency.task_id == task.id)
            .all()
        )

        blocked = False

        for dependency in dependencies:

            dependency_task = (
                db.query(Task)
                .filter(Task.id == dependency.depends_on_task_id)
                .first()
            )

            if (
                dependency_task
                and dependency_task.status != "completed"
            ):
                blocked = True
                break

        if not blocked:
            available_tasks.append(task)

    available_tasks.sort(
        key=lambda task: (
            PRIORITY_ORDER.get(task.priority, 0),
            task.estimated_hours or 0,
        ),
        reverse=True,
    )

    return available_tasks

def generate_productivity_plan(
    role: str,
    db: Session
) -> ProductivityPlan:
    """
    Generate an AI daily productivity plan for a given role.
    """

    tasks = get_tasks_for_role(
        role=role,
        db=db,
    )
    if not tasks:
        return ProductivityPlan(
            summary=f"No active tasks found for {role}.",
            total_hours=0,
            tasks=[],
            risks=[],
        )
    formatted_tasks = "\n\n".join(
        [
            f"""
Title: {task.title}
Description: {task.description}
Priority: {task.priority}
Estimated Hours: {task.estimated_hours}
"""
            for task in tasks
        ]
    )
    plan = llm.invoke(
        PRODUCTIVITY_PROMPT.format(
            role=role,
            tasks=formatted_tasks,
        )
    )
    return plan