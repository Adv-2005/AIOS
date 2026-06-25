from langchain_community.document_loaders import PyPDFLoader


def extract_requirement(file_path: str) -> str:
    """
    Extract the full requirement text from a PDF.
    No chunking or embeddings are performed.
    """

    loader = PyPDFLoader(file_path)
    pages = loader.load()

    requirement = "\n\n".join(
        page.page_content
        for page in pages
    )

    return requirement