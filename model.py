from langchain_google_genai import ChatGoogleGenerativeAI
from embeddings import api_key
model=ChatGoogleGenerativeAI(model='gemini-3.1-flash-lite-preview',google_api_key=api_key)
