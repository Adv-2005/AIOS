

from sqlalchemy import Column, ForeignKey, Integer
import uuid
from app.database.session import Base
from sqlalchemy.dialects.postgresql import UUID


class TaskDependency(Base):
    __tablename__ = "task_dependencies"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    task_id = Column(
        UUID(as_uuid=True),
        ForeignKey("tasks.id"),
        nullable=False
    )

    depends_on_task_id = Column(
        UUID(as_uuid=True),
        ForeignKey("tasks.id"),
        nullable=False
    )
    