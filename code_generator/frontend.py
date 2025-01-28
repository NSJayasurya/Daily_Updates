from langchain_groq import ChatGroq
from dotenv import load_dotenv
from model import create_chat_groq
import chain
load_dotenv()
import streamlit as st

def code_generator_app():
    with st.form("Code_generator"):
        topic = st.text_input("Enter the question for which you need a code")
        language = st.text_input("Enter the programming language you want the code in")
        submitted = st.form_submit_button("Submit")
        
        if submitted:
            if not topic or not language:
                st.warning("Please enter both the question and the programming language.")
            else:
                try:
                    response = chain.generate_code(topic, language)
                    st.info(response)
                except Exception as e:
                    st.error(f"An error occurred: {e}")

code_generator_app()
