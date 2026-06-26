from typing import TypedDict

from app.schemas.productivity import ProductivityPlan


class ProductivityState(TypedDict):
    role: str
    productivity_plan: ProductivityPlan