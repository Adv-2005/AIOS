# app/schemas/strategy.py

from pydantic import BaseModel


class ProjectRisk(BaseModel):
    project: str
    reason: str


class PriorityWork(BaseModel):
    task: str
    reason: str


class IndustryUpdate(BaseModel):
    title: str
    summary: str
    business_impact: str


class MondaySessionReport(BaseModel):
    executive_summary: str

    projects_at_risk: list[ProjectRisk]

    high_priority_work: list[PriorityWork]

    key_risks: list[str]

    recommendations: list[str]

    next_week_priorities: list[str]

    industry_updates: list[IndustryUpdate]


class MondaySessionRequest(BaseModel):
    """
    Empty for now since the report is generated
    from current company data.

    Can later be extended with:
    - department
    - date
    - include_web_updates
    - include_company_brain
    """
    pass