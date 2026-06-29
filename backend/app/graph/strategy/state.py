from typing import TypedDict

from app.schemas.strategy import MondaySessionReport


class StrategyState(TypedDict):
    monday_session: MondaySessionReport