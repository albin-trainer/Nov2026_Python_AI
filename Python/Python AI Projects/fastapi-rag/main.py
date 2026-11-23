from fastapi import FastAPI
from config import create_vector_store

from service import generate_answer

app = FastAPI()

vector_store = create_vector_store() ##Vector is created


@app.get("/search")
def search(query: str):

    results = vector_store.search(query)

    return results

#
@app.get("/chat")
def chat(prompt: str):

   #Retrived top k chunks
    documents = vector_store.search(
        prompt,
        top_k=3
    )

#Augmented
    answer = generate_answer(
        prompt,
        documents
    )

    return {
        "question": prompt,
        "answer": answer
    }
