# models/kpi.py

import uuid

from sqlalchemy import (
    Column,
    String,
    Float,
    DateTime,
    ForeignKey
)

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from app.database.session import Base


class KPI(Base):
    __tablename__ = "kpis"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    employee_id = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id")
    )

    metric_name = Column(
        String,
        nullable=False
    )

    metric_value = Column(
        Float,
        nullable=False
    )

    recorded_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )