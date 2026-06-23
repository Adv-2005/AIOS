from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.models.document import Document
from app.models.chunk import Chunk
from app.services.vectorstore import get_vectorstore


def ingest_document(
    file_path: str,
    filename: str,
    db
):
    try:

        loader = PyPDFLoader(file_path)
        pages = loader.load()

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )

        chunks = splitter.split_documents(pages)

        document = Document(
            filename=filename,
            file_path=file_path
        )

        db.add(document)
        db.commit()
        db.refresh(document)

        for idx, chunk in enumerate(chunks):

            db_chunk = Chunk(
                document_id=document.id,
                chunk_index=idx,
                content=chunk.page_content
            )

            db.add(db_chunk)

            chunk.metadata.update(
                {
                    "document_id": str(document.id),
                    "filename": filename,
                    "chunk_index": idx
                }
            )

        db.commit()

        vectorstore = get_vectorstore()
        vectorstore.add_documents(chunks)

        return str(document.id)

    except Exception as e:
        db.rollback()
        raise e