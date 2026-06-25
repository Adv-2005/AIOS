

from app.graph.project.state import ProjectState
from app.services.project_planner import generate_project_plan


def planner_node(state: ProjectState):

    plan = generate_project_plan(
        state["requirement"]
    )

    return {
        "project_plan": plan
    }