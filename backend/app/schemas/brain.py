from pydantic import BaseModel


class BrainRequest(BaseModel):
    question: str