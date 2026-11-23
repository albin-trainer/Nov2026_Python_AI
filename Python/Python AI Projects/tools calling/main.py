from fastapi import FastAPI
from ai_controller import chat

app = FastAPI()

@app.get("/chat")

def chat_endpoint(prompt: str):

    answer = chat(prompt)

    return {
        "answer": answer
    }