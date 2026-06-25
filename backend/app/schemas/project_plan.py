from pydantic import BaseModel


class TaskPlan(BaseModel):
    title: str
    description: str
    priority: str
    estimate_hours: int


class MilestonePlan(BaseModel):
    name: str
    description: str


class ProjectPlan(BaseModel):
    project_name: str
    summary: str

    milestones: list[MilestonePlan]

    tasks: list[TaskPlan]

    risks: list[str]


class ProjectRequest(BaseModel):
    requirement: str