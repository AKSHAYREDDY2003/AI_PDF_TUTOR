from langchain_community.vectorstores import Chroma
from embeddings import embeddings

def create_vector_store(chunks, persist_dir):

    clean_chunks = [
        c for c in chunks
        if c and c.page_content and c.page_content.strip()
    ]

    vectordb = Chroma.from_documents(
        documents=clean_chunks,
        embedding=embeddings,
        persist_directory=persist_dir
    )

    return vectordb

def get_retriever(persist_dir):

    vectordb = Chroma(
        persist_directory=persist_dir,
        embedding_function=embeddings
    )

    return vectordb.as_retriever(search_kwargs={"k":10})






























































































