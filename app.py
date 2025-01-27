from langchain_groq import ChatGroq
from dotenv import load_dotenv
from model import create_chat_groq
import chain
load_dotenv()
import streamlit as st
# llm = ChatGroq(
#     model="mixtral-8x7b-32768",
#     temperature=0,
#     max_tokens=None,
#     timeout=None,
#     max_retries=2
# )


# llm=create_chat_groq()
# response = llm.invoke("Hi")
# print(response.content)
def poem_generator_app():
    with st.form("poem_generator"):
        topic=st.text_input("Enter topic for the poem")
        submitted=st.form_submit_button("Submit")
        if(submitted):
            response =chain.generate_poem(topic)
            st.info(response)
poem_generator_app()