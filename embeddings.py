from langchain_google_genai import GoogleGenerativeAIEmbeddings

import os

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001",
    google_api_key=api_key
)
