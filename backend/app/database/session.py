from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

print(f"DATABASE_URL = {settings.DATABASE_URL}")
engine = create_engine(
    settings.DATABASE_URL,
    echo=True
)

SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False
)

Base = declarative_base()