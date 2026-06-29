from fastapi import FastAPI
from app.api.routes import documents
from app.api.routes import brain
from app.api.routes import project
from app.api.routes import productivity
from app.api.routes import strategy
from app.api.routes import kpi

app = FastAPI(title="AI Command Centre",
    description="An AI-powered command centre for your company")


app.include_router(
    documents.router,
    prefix="/documents",
    tags=["Documents"]
)

app.include_router(
    brain.router,
    prefix="/brain",
    tags=["Brain"]
)

app.include_router(
    project.router,
    prefix="/project",
    tags=["Project"]
)

app.include_router(
    productivity.router,
    prefix="/productivity",
    tags=["Productivity"]
)

app.include_router(
    strategy.router,
    prefix="/strategy",
    tags=["Strategy"]
)

app.include_router(
    kpi.router,
    prefix="/kpi",
    tags=["KPI"]
)
