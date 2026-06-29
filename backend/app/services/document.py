# app/services/document.py

from sqlalchemy.orm import Session

from app.models.document import Document


def get_documents(db: Session):

    documents = (
        db.query(Document)
        .order_by(Document.created_at.desc())
        .all()
    )

    return [
        {
            "id": str(doc.id),
            "filename": doc.filename
        }
        for doc in documents
    ]