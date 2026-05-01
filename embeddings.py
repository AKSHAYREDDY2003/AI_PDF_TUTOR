from langchain_google_genai import GoogleGenerativeAIEmbeddings
import streamlit as st
api_key = st.secrets.get("GOOGLE_API_KEY")
embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-2",
    google_api_key=api_key
)
