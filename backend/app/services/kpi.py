from sqlalchemy.orm import Session
from sqlalchemy import func

from app.models.project import Project
from app.models.task import Task
from app.models.task_dependencies import TaskDependency

from app.schemas.kpi import (
    OverviewMetrics,
    TaskMetrics,
    PriorityMetrics,
    TeamProductivity,
    TrendPoint,
    DashboardResponse
)


def get_overview_metrics(db: Session):

    total_projects = db.query(Project).count()

    active_projects = (
        db.query(Project)
        .filter(Project.status != "completed")
        .count()
    )

    completed_projects = (
        db.query(Project)
        .filter(Project.status == "completed")
        .count()
    )

    project_completion = (
        (completed_projects / total_projects) * 100
        if total_projects > 0 else 0
    )

    return OverviewMetrics(
        total_projects=total_projects,
        active_projects=active_projects,
        completed_projects=completed_projects,
        project_completion_percentage=round(project_completion, 1)
    )


def get_task_metrics(db: Session):

    total = db.query(Task).count()

    completed = (
        db.query(Task)
        .filter(Task.status == "completed")
        .count()
    )

    in_progress = (
        db.query(Task)
        .filter(Task.status == "in_progress")
        .count()
    )

    pending = (
        db.query(Task)
        .filter(Task.status == "todo")
        .count()
    )

    return TaskMetrics(
        total_tasks=total,
        completed_tasks=completed,
        in_progress_tasks=in_progress,
        pending_tasks=pending
    )


def get_priority_metrics(db: Session):

    high = (
        db.query(Task)
        .filter(func.lower(Task.priority) == "high")
        .count()
    )

    medium = (
        db.query(Task)
        .filter(func.lower(Task.priority) == "medium")
        .count()
    )

    low = (
        db.query(Task)
        .filter(func.lower(Task.priority) == "low")
        .count()
    )

    return PriorityMetrics(
        high=high,
        medium=medium,
        low=low
    )


def get_blocked_tasks(db: Session):

    blocked = 0

    dependencies = db.query(TaskDependency).all()

    for dependency in dependencies:

        depends_on = (
            db.query(Task)
            .filter(Task.id == dependency.depends_on_task_id)
            .first()
        )

        if depends_on and depends_on.status != "completed":
            blocked += 1

    return blocked


def get_team_productivity():

    return [
        TeamProductivity(
            team="Backend",
            productivity=82
        ),
        TeamProductivity(
            team="Frontend",
            productivity=74
        ),
        TeamProductivity(
            team="AI/ML",
            productivity=91
        )
    ]


def get_trend_data():

    return [
        TrendPoint(
            week="Week 1",
            completion=42
        ),
        TrendPoint(
            week="Week 2",
            completion=58
        ),
        TrendPoint(
            week="Week 3",
            completion=71
        ),
        TrendPoint(
            week="Week 4",
            completion=89
        )
    ]


def get_dashboard(db: Session):

    return DashboardResponse(
        overview=get_overview_metrics(db),
        tasks=get_task_metrics(db),
        priorities=get_priority_metrics(db),
        blocked_tasks=get_blocked_tasks(db),
        team_productivity=get_team_productivity(),
        trend=get_trend_data()
    )