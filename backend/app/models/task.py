# models/task.py

import uuid

from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    DateTime,
    ForeignKey
)

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from app.database.session import Base


class Task(Base):
    __tablename__ = "tasks"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    project_id = Column(
        UUID(as_uuid=True),
        ForeignKey("projects.id")
    )

    assignee_id = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id")
    )

    title = Column(String)

    description = Column(Text)

    priority = Column(
        String,
        default="medium"
    )

    status = Column(
        String,
        default="todo"
    )

    due_date = Column(DateTime)
    estimated_hours = Column(Integer)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )   

    suggested_role = Column(String)