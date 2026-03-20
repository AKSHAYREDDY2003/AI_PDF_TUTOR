from langchain_text_splitters import RecursiveCharacterTextSplitter

def doc_splitter(documents):
    text_splitter=RecursiveCharacterTextSplitter(
    chunk_size=500,chunk_overlap=50)
    chunks=text_splitter.split_documents(documents)
    return chunks
