# models/project.py

import uuid

from sqlalchemy import (
    Column,
    String,
    Text,
    DateTime
)

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from app.database.session import Base


class Project(Base):
    __tablename__ = "projects"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    name = Column(String)

    description = Column(Text)

    status = Column(
        String,
        default="planned"
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )