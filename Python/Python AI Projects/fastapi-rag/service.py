from openai import OpenAI

from aiconfig import client


def generate_answer(question, documents):

    context = "\n\n".join(document["content"]
        for document in documents
    )

    prompt = f"""
You are an HR assistant.

Answer the question using only the provided HR policy.

If the answer is not available in the policy,
say that the information is not available.

HR POLICY:
{context}

QUESTION:
{question}
"""

    response = client.responses.create(
        model="gpt-5.6-luna",
        input=prompt
    )

    return response.output_text