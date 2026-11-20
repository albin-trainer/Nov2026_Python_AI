from pathlib import Path

from rag import read_document
from splitter import split_text
from vectorstore import SimpleVectorStore


VECTOR_FILE = "vector_store_hr.json"


def create_vector_store():

    vector_store = SimpleVectorStore(VECTOR_FILE)

    if Path(VECTOR_FILE).exists():

        print("Loaded Vector Store File!")

        vector_store.load()

    else:

        print("Create Vector File")

        document = read_document("hrpolicy.txt")

        chunks = split_text(
            document["content"],
            chunk_size=50,
            overlap=10
        )

        vector_store.add(chunks)

        vector_store.save()

    return vector_store