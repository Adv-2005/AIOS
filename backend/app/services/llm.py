from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
from app.core.config import settings


def get_llm():
    return ChatGroq(model="llama-3.1-8b-instant", temperature=0, api_key=settings.GROQ_API_KEY)
