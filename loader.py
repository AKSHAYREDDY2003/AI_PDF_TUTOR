from langchain_community.document_loaders import PyPDFLoader
def file_loader(path):
    loader=PyPDFLoader(path)
    documents=loader.load()
    return documents