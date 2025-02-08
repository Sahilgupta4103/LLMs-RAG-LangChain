from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import ollama
from langchain_community.chat_models import ChatOllama

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()


os.environ["LANGCHAIN_TRACING_V2"]="true"  ##this is feature is for langsmith for tracing all the queries and backend handeling.
os.environ["LANGCHAIN_API_KEY"]="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"

#prompt template

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "you are a helpful assistant. please respond to the queries"),
        ("user","Question:{question}"),
    ]
)

##streamlit framework

st.title("Langchain Practise with OLLAMA")
input_text=st.text_input("Search your queries here")


llm = ChatOllama(model="llama3.2:latest")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question': input_text}))
