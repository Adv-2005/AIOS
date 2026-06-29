from pathlib import Path

from fastapi import APIRouter, Form
from fastapi import UploadFile
from fastapi import File
from fastapi import Depends

from sqlalchemy.orm import Session

from app.api.deps import get_db

from app.services.ingestion import (
    ingest_document
)
from app.services.document import get_documents

router = APIRouter()

@router.get("/")
def list_documents(
    db: Session = Depends(get_db)
):
    return get_documents(db)

@router.post("/upload")
async def upload_document(file: UploadFile = File(...),visibility: str = Form("app"),department: str | None = Form(None),db: Session = Depends(get_db) ):
    Path("uploads").mkdir(exist_ok=True)
    file_path = f"uploads/{file.filename}"

    with open(file_path, "wb") as f:
        f.write(await file.read())
    document_id = ingest_document(file_path=file_path,filename=file.filename,visibility=visibility,department=department,db=db)
    return {
    "message": "uploaded",
    "document_id": document_id
}