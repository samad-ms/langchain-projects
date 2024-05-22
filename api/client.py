import streamlit as st
import requests

def openai_response(input_text):
    response=requests.post('http://localhost:8000/essay/invoke',
                           json={"input": {"topic": input_text}})
    return response.json()['output']['content']

def ollama_response(input_text):
    response=requests.post('http://localhost:8000/poem/invoke',
                           json={"input": {"topic": input_text}})
    return response.json()['output']

st.set_page_config(page_title='bot')
st.header('bot for writing essay and poem')
input1=st.text_input('essay on the topic: ')
input2=st.text_input('poem on the topic: ')

if input1:
    st.write(openai_response(input1))
if input2:
    st.write(ollama_response(input2))