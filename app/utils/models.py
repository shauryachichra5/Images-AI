from dotenv import load_dotenv
from langchain_groq import ChatGroq
import os

load_dotenv(override=True)
MODEL=os.getenv("GROQ_MODEL")
ACCESS_KEY=os.getenv("GROQ_API_KEY")

llm = ChatGroq(
    model=MODEL,
    temperature=0,
    max_tokens=None,
    reasoning_format="parsed",
    timeout=None,
    max_retries=2,
    api_key=ACCESS_KEY
    # other params...
)