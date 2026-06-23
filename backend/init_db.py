# init_db.py

from app.database.session import engine
from app.models import *
from app.database.session import Base
import app.models
print(engine.url)

with engine.connect() as conn:
    print("Connected successfully!")
Base.metadata.create_all(
    bind=engine
)