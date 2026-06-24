from rank_bm25 import BM25Okapi

from app.database.session import SessionLocal
from app.models.chunk import Chunk


def build_bm25():

    db = SessionLocal()

    chunks = db.query(Chunk).all()

    corpus = [
        chunk.content.split()
        for chunk in chunks
    ]

    bm25 = BM25Okapi(corpus)

    return bm25, chunks