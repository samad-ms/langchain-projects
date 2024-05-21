from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from dotenv import load_dotenv
load_dotenv()

import os 
import streamlit as st
# from langchain_openai import ChatOpenAI

os.environ['OPENAI_API_KEY']=os.getenv('OPENAI_API_KEY')
os.environ['LANGCHAIN_API_KEY']=os.getenv('LANGCHAIN_API_KEY')
os.environ['LANGCHAIN_TRACING_V2']='true'
#1
prompt=ChatPromptTemplate.from_messages([
        ("system","you are an helpful assistant. please respond to user questions"),
        ("user","{question}")
    ])

st.set_page_config(page_title='chatbot')
input=st.text_input('type your question',key='input')
submit=st.button('ask your question')
#2
llm=ChatOpenAI(model="gpt-3.5-turbo")
#3
ouput_parser=StrOutputParser()
##
chain=prompt|llm|ouput_parser

if submit:
    st.write(chain.invoke({'question':input}))


