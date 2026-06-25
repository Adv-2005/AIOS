from langgraph.graph import StateGraph
from langgraph.graph import START
from langgraph.graph import END


from app.graph.project.nodes.planner_node import planner_node
from app.graph.project.state import ProjectState

def build_project_graph():

    builder = StateGraph(ProjectState)

    builder.add_node(
        "planner",
        planner_node
    )

    builder.add_edge(
        START,
        "planner"
    )

    builder.add_edge(
        "planner",
        END
    )

    return builder.compile()
