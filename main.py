from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from langchain_community.chat_models import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatInput(BaseModel):
    message: str

@app.post("/chat")
async def chat_endpoint(input: ChatInput):
    openai_key = os.getenv("OPENAI_API_KEY")
    chat = ChatOpenAI(openai_api_key=openai_key)
    response = chat.predict(input.message)
    return {"response": response}
