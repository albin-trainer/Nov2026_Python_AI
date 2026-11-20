import json
import numpy as np
from openai import OpenAI
from aiconfig import client


class SimpleVectorStore:

    def __init__(self, filename):

        self.filename = filename

        self.client =client

        self.documents = []

    def add(self, chunks):

        for chunk in chunks:

            response = self.client.embeddings.create(
                model="text-embedding-3-small",
                input=chunk
            )

            embedding = response.data[0].embedding

            self.documents.append({
                "content": chunk,
                "embedding": embedding
            })

    def save(self):

        with open(self.filename, "w", encoding="utf-8") as file:

            json.dump(self.documents, file)

    def load(self):

        with open(self.filename, "r", encoding="utf-8") as file:

            self.documents = json.load(file)

    def similarity(self, a, b):

        a = np.array(a)
        b = np.array(b)

        return np.dot(a, b) / (
            np.linalg.norm(a) * np.linalg.norm(b)
        )
    def search(self, query, top_k=3):

        response = self.client.embeddings.create(
            model="text-embedding-3-small",
            input=query
        )

        query_embedding = response.data[0].embedding

        results = []

        for document in self.documents:

            score = self.similarity(
                query_embedding,
                document["embedding"]
            )

            results.append({
                "content": document["content"],
                "score": score
            })

        results.sort(
            key=lambda x: x["score"],
            reverse=True
        )

        return results[:top_k]