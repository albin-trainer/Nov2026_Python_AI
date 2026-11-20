from fastapi import  FastAPI

app=FastAPI()
@app.get("/hello")
def sayHello():
    return "Hi Have a Wornderful Evening"


@app.get("/chat")
def chat(prompt:str):
    #connect with LLM and get the resp and return to the Client
    return f"Prompt entered is {prompt} "




print(sayHello())