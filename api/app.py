from langchain_openai import ChatOpenAI
from langchain_community.llms import Ollama
from langchain.prompts import ChatPromptTemplate

from fastapi import FastAPI
from langserve import add_routes
import uvicorn

import os 
from dotenv import load_dotenv
load_dotenv()

os.environ['OPENAI_API_KEY']=os.getenv('OPENAI_API_KEY')

prompt1=ChatPromptTemplate.from_template('write a essay on {topic} within 100 words')
prompt2=ChatPromptTemplate.from_template('write a poem on {topic} within 100 words')

model1=ChatOpenAI()
model2=Ollama()

app=FastAPI(
    title="Langchain server",
    version="1.0",
    description="simple langchain server"
)

add_routes(
    app,
    ChatOpenAI(),
    path='/openai'
)
add_routes(
    app,
    prompt1|model1,
    path='/essay'
)
add_routes(
    app,
    prompt2|model2,
    path='/poem'
)

if __name__=='__main__':
    uvicorn.run(app,host='localhost',port=8000)