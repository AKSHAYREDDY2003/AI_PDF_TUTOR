def format_docs(docs):
    return '\n\n'.join(doc.page_content for doc in docs)

    
from langchain.memory import RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory


import streamlit as st
def get_session_history(session_id):
    if "chat_store" not in st.session_state:
        st.session_state.chat_store = {}

    if session_id not in st.session_state.chat_store:
        st.session_state.chat_store[session_id] = InMemoryChatMessageHistory()

    return st.session_state.chat_store[session_id]



from  prompts import prompt_template
from model import model



def run_rag(inputs):
    question = inputs["question"]
    retriever = inputs["retriever"]
    docs=retriever.invoke(question)
    context=format_docs(docs)
    return context
from operator import itemgetter
chain = {'context': run_rag , 'question': itemgetter('question'),
        'history': itemgetter("history")   }  | prompt_template | model 

chain_with_history = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="question",
    history_messages_key="history"
)

