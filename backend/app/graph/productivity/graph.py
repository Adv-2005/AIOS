

from langgraph.graph import END, START, StateGraph

from app.graph.productivity.state import ProductivityState
from app.graph.productivity.nodes import planner_node


builder = StateGraph(ProductivityState)

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

graph = builder.compile()