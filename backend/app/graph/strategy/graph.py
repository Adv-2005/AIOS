from langgraph.graph import (
    START,
    END,
    StateGraph,
)

from app.graph.strategy.state import (
    StrategyState,
)

from app.graph.strategy.nodes import (
    planner_node,
)


builder = StateGraph(
    StrategyState
)

builder.add_node(
    "planner",
    planner_node,
)

builder.add_edge(
    START,
    "planner",
)

builder.add_edge(
    "planner",
    END,
)

graph = builder.compile()