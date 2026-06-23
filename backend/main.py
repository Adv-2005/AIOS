from fastapi import FastAPI
from app.api.routes import documents
from app.api.routes import brain
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