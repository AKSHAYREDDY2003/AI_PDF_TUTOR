from langchain_google_genai import ChatGoogleGenerativeAI
import os

api_key = os.getenv("GOOGLE_API_KEY")
model=ChatGoogleGenerativeAI(model='gemini-3.1-flash-lite-preview',google_api_key=api_key)
