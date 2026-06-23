from app.api.routes import documents
from fastapi import FastAPI
app = FastAPI(title="AI Command Centre",
    description="An AI-powered command centre for your company")


app.include_router(
    documents.router,
    prefix="/documents",
    tags=["Documents"]
)