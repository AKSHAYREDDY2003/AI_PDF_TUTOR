import streamlit as st
from gtts import gTTS
import uuid
import os

from loader import file_loader
from splitter import doc_splitter
from vector_store import create_vector_store, get_retriever
from rag_pipeline import chain_with_history


st.title("📄 AI PDF Tutor")

# create user session id
if "user_id" not in st.session_state:
    st.session_state.user_id = str(uuid.uuid4())

user_id = st.session_state.user_id

# upload pdf
uploaded_file = st.file_uploader("Upload your PDF", type="pdf")

# check if pdf uploaded
if uploaded_file:

    if "processed" not in st.session_state:

        st.success("PDF uploaded successfully")

        with open("temp.pdf", "wb") as f:
            f.write(uploaded_file.getvalue())

        docs = file_loader("temp.pdf")
        chunks = doc_splitter(docs)

        persist_dir = f"vector_db/{user_id}"
        create_vector_store(chunks, persist_dir)

        st.session_state.processed = True
        st.session_state.persist_dir = persist_dir

    persist_dir = st.session_state.persist_dir
    retriever = get_retriever(persist_dir)
    
    # show question box only after pdf upload
    question = st.chat_input("Ask a question about the PDF")

    if question:
        response = chain_with_history.invoke(
            {"question": question,
             "retriever":retriever},
            config={"configurable": {"session_id": user_id}}
        )
        text = response.content[0]["text"]

        st.write(text)
        
        tts = gTTS(text)

        tts.save("voice.mp3")

        st.audio("voice.mp3")
    

else:

    st.info("Please upload a PDF before asking questions.")
