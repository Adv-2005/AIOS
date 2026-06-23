# models/chunk.py

import uuid

from sqlalchemy import (
    Column,
    Integer,
    Text,
    ForeignKey
)

from sqlalchemy.dialects.postgresql import UUID

from app.database.session import Base


class Chunk(Base):
    __tablename__ = "chunks"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    document_id = Column(
        UUID(as_uuid=True),
        ForeignKey("documents.id"),
        nullable=False
    )

    chunk_index = Column(
        Integer,
        nullable=False
    )

    content = Column(
        Text,
        nullable=False
    )