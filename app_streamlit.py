# app_streamlit.py
import streamlit as st
from dotenv import load_dotenv
load_dotenv()

from agent import (
    load_csv_to_docs,
    chunk_texts,
    build_vector_store,
    build_qa_chain,
    query_assistant
)

st.set_page_config(page_title="Research Assistant", layout="wide")

st.title("Research Assistant - Llama (Groq)")

uploaded_file = st.file_uploader("Subí un CSV para iniciar el análisis", type=["csv"])

if uploaded_file:
    with st.spinner("Procesando CSV..."):
        docs = load_csv_to_docs(uploaded_file)
        chunks = chunk_texts(docs)
        vector_store = build_vector_store(chunks)
        qa_chain = build_qa_chain(vector_store)

    st.success("CSV procesado y modelo listo para consultas.")

    question = st.text_input("Ingresá tu pregunta:")

    if question:
        with st.spinner("Consultando al modelo..."):
            answer = query_assistant(qa_chain, question)

        st.subheader("Respuesta")
        st.write(answer)
else:
    st.info("Esperando que subas un archivo CSV.")
