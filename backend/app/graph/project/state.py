from typing import TypedDict

class ProjectState(TypedDict):
    requirement: str
    project_plan: dict
    project_id: str | None