# app/services/strategy.py

from sqlalchemy.orm import Session

from langchain_tavily import TavilySearch

from app.models.project import Project
from app.models.task import Task
from app.models.task_dependencies import TaskDependency

from app.schemas.strategy import MondaySessionReport

from app.services.llm import get_project_planner_llm
from app.graph.strategy.prompts import MONDAY_SESSION_PROMPT


llm = get_project_planner_llm().with_structured_output(
    MondaySessionReport
)

tavily = TavilySearch(
    max_results=5,
    tavily_api_key="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"
)


def get_company_context(db: Session) -> str:
    """
    Collect current company operational data
    for the Monday leadership session.
    """

    projects = db.query(Project).all()
    tasks = db.query(Task).all()

    project_summary = []

    for project in projects:

        project_tasks = [
            task
            for task in tasks
            if task.project_id == project.id
        ]

        completed = len(
            [
                t
                for t in project_tasks
                if t.status == "completed"
            ]
        )

        high_priority = len(
            [
                t
                for t in project_tasks
                if (
                    t.priority == "High"
                    and t.status != "completed"
                )
            ]
        )

        blocked = 0

        for task in project_tasks:

            dependencies = (
                db.query(TaskDependency)
                .filter(
                    TaskDependency.task_id == task.id
                )
                .all()
            )

            for dependency in dependencies:

                dependency_task = (
                    db.query(Task)
                    .filter(
                        Task.id == dependency.depends_on_task_id
                    )
                    .first()
                )

                if (
                    dependency_task
                    and dependency_task.status != "completed"
                ):
                    blocked += 1
                    break

        project_summary.append(
            f"""
Project:
{project.name}

Status:
{project.status}

Completed Tasks:
{completed}

Pending Tasks:
{len(project_tasks) - completed}

High Priority Remaining:
{high_priority}

Blocked Tasks:
{blocked}
"""
        )

    high_priority_tasks = [
        task
        for task in tasks
        if (
            task.priority == "High"
            and task.status != "completed"
        )
    ]

    task_summary = "\n".join(
        [
            f"""
Title: {task.title}
Role: {task.suggested_role}
Priority: {task.priority}
Status: {task.status}
Estimated Hours: {task.estimated_hours}
"""
            for task in high_priority_tasks
        ]
    )

    return f"""
Projects

{"".join(project_summary)}

High Priority Tasks

{task_summary}
"""


def get_industry_updates() -> str:
    """
    Fetch latest AI / software industry news.
    """

    results = tavily.invoke(
        {
            "query": """
Latest AI news,
software engineering,
developer tools,
cloud computing,
cybersecurity,
LLMs,
GenAI announcements
"""
        }
    )

    return str(results)


def generate_monday_session(
    db: Session,
) -> MondaySessionReport:
    """
    Generate the executive Monday Session report.
    """

    company_context = get_company_context(db)

    industry_updates = get_industry_updates()

    report = llm.invoke(
        MONDAY_SESSION_PROMPT.format(
            company_context=company_context,
            industry_updates=industry_updates,
        )
    )

    return report