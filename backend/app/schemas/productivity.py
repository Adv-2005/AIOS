

from pydantic import BaseModel

class DailyTask(BaseModel):

    title: str

    reason: str

    estimated_hours: int

class ProductivityPlan(BaseModel):

    summary: str

    total_hours: int

    tasks: list[DailyTask]

    risks: list[str]

class ProductivityRequest(BaseModel):
    role: str