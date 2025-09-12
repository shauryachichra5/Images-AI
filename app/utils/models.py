from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
import os

load_dotenv(override=True)
GROQ_MODEL=os.getenv("GROQ_MODEL")
OPENAI_MODEL=os.getenv("OPENAI_MODEL")
ACCESS_KEY=os.getenv("GROQ_API_KEY")
OPENAI_KEY=os.getenv("OPENAI_KEY")

llm_groq = ChatGroq(
    model=GROQ_MODEL,
    temperature=0.75,
    max_tokens=None,
    reasoning_format="parsed",
    timeout=None,
    max_retries=2,
    api_key=ACCESS_KEY
    # other params...
)
llm_openai = ChatOpenAI(
    model = OPENAI_MODEL,
    openai_api_key = OPENAI_KEY,
    temperature=0.75
)

# ----LLM in use----
llm = llm_openai