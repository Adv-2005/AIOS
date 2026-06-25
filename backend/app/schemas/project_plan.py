from langchain_protocol import Literal
from pydantic import BaseModel, Field


class TaskPlan(BaseModel):
    task_id: int = Field(..., description="Unique identifier for the task, starting from 1.")
    title: str
    description: str
    priority: Literal["Low", "Medium", "High"]
    estimated_hours: int
    depends_on: list[int] = Field(default_factory=list, description="List of task_ids that must be completed first. Empty list if no dependencies.")


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