from langchain_core.runnables import RunnableConfig

from app.graph.strategy.state import StrategyState

from app.services.strategy import (
    generate_monday_session,
)


def planner_node(
    state: StrategyState,
    config: RunnableConfig,
):
    db = config["configurable"]["db"]

    report = generate_monday_session(
        db=db
    )

    return {
        "monday_session": report
    }