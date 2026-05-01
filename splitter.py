from langchain_text_splitters import RecursiveCharacterTextSplitter

def doc_splitter(documents):
    text_splitter=RecursiveCharacterTextSplitter(
    chunk_size=500,chunk_overlap=50)
    chunks = text_splitter.split_documents(documents)

    # ✅ CLEAN chunks (IMPORTANT FIX)
    clean_chunks = [
        c for c in chunks
        if c and c.page_content and c.page_content.strip()
    ]

    print("Total chunks:", len(chunks))
    print("Clean chunks:", len(clean_chunks))

    return clean_chunks
