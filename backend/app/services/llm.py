from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
from app.core.config import settings


def get_query_rewrite_llm():
    return ChatGroq(model="llama-3.1-8b-instant", temperature=0, api_key=settings.GROQ_API_KEY)


def get_project_planner_llm():
    return ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0,
        google_api_key=settings.GEMINI_API_KEY,
    )


def get_llm():
    return get_query_rewrite_llm()
