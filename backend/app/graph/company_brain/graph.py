from langgraph.graph import StateGraph
from langgraph.graph import START
from langgraph.graph import END

from app.graph.company_brain.state import BrainState

from app.graph.company_brain.nodes.retrieve_node import retrieve_node
from app.graph.company_brain.nodes.answer_node import answer_node


def build_company_brain():

    builder = StateGraph(BrainState)

    builder.add_node(
        "retrieve",
        retrieve_node
    )

    builder.add_node(
        "answer",
        answer_node
    )

    builder.add_edge(
        START,
        "retrieve"
    )

    builder.add_edge(
        "retrieve",
        "answer"
    )

    builder.add_edge(
        "answer",
        END
    )

    return builder.compile()