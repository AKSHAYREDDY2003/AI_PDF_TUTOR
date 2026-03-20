from langchain_community.vectorstores import Chroma
from embeddings import embeddings

def create_vector_store(chunks, persist_dir):

    vectordb = Chroma.from_documents(
        documents=chunks,
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






























































































