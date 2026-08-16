from re import S
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from ai_api import get_ai_response
from pydantic import BaseModel

class UserMessage(BaseModel):
    text: str
    status: bool 

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ['*'],
    allow_headers = ['*']
)

@app.post('/message')
def message(data: UserMessage):
    answer = get_ai_response(text=data.text, passport_received=data.status)
    return {
        "role": "assistant",
        "content": answer,
    }