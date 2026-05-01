from langchain_text_splitters import RecursiveCharacterTextSplitter

def doc_splitter(documents):
    text_splitter=RecursiveCharacterTextSplitter(
    chunk_size=500,chunk_overlap=50)
    chunks = text_splitter.split_documents(documents)

    # ✅ CLEAN chunks (IMPORTANT FIX)
    clean_chunks = []
    for c in chunks:
        if c and c.page_content and c.page_content.strip():
            clean_chunks.append(c)

    print("Before:", len(chunks))
    print("After :", len(clean_chunks))

    return clean_chunks
