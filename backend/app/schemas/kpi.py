from pydantic import BaseModel


class OverviewMetrics(BaseModel):
    total_projects: int
    active_projects: int
    completed_projects: int
    project_completion_percentage: float


class TaskMetrics(BaseModel):
    total_tasks: int
    completed_tasks: int
    in_progress_tasks: int
    pending_tasks: int


class PriorityMetrics(BaseModel):
    high: int
    medium: int
    low: int


class TeamProductivity(BaseModel):
    team: str
    productivity: int


class TrendPoint(BaseModel):
    week: str
    completion: int


class DashboardResponse(BaseModel):
    overview: OverviewMetrics
    tasks: TaskMetrics
    priorities: PriorityMetrics
    blocked_tasks: int
    team_productivity: list[TeamProductivity]
    trend: list[TrendPoint]