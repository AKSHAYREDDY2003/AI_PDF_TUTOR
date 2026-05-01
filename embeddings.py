from langchain_google_genai import GoogleGenerativeAIEmbeddings
import streamlit as st
api_key = st.secrets.get("GOOGLE_API_KEY")
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001",
    google_api_key=api_key
)
