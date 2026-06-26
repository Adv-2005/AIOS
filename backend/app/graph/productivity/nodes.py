from sqlalchemy.orm import Session
from langchain_core.runnables import RunnableConfig
from app.graph.productivity.state import ProductivityState
from app.schemas.productivity import ProductivityPlan
from app.services.llm import get_project_planner_llm
from app.services.productivity import generate_productivity_plan

llm = get_project_planner_llm().with_structured_output(ProductivityPlan)


def planner_node(
    state: ProductivityState,
    config: RunnableConfig,
):
    db = config["configurable"]["db"]
    plan = generate_productivity_plan(
        role=state["role"],
        db=db
    )

    return {
        "productivity_plan": plan
    }
    