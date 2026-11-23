import os
import json

from openai import OpenAI
from dotenv import load_dotenv

from tools import get_weather, book_flight

load_dotenv(override=True)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
weather_tool = {
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "Get the current weather of a city",
        "parameters": {
            "type": "object",
            "properties": {
                "city": {
                    "type": "string",
                    "description": "Name of the city"
                }
            },
            "required": ["city"]
        }
    }
}
flight_tool = {
    "type": "function",
    "function": {
        "name": "book_flight",
        "description": "Book a flight to a destination city",
        "parameters": {
            "type": "object",
            "properties": {
                "destination": {
                    "type": "string",
                    "description": "Destination city"
                }
            },
            "required": ["destination"]
        }
    }
}

tools = [
    weather_tool,
    flight_tool
]
def chat(prompt: str):

    messages = [
        {
            "role": "user",
            "content": prompt
        }
    ]

    while True:

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            tools=tools
        )
        # LLM's response
        message = response.choices[0].message

        # No tool required
        if not message.tool_calls:

            return message.content

        # Add assistant's tool request to conversation
        messages.append(message)

        # Execute requested tools
        for tool_call in message.tool_calls:

            tool_name = tool_call.function.name

            arguments = json.loads(
                tool_call.function.arguments
            )

            print("Calling tool:", tool_name)
            print("Arguments:", arguments)

            if tool_name == "get_weather":

                result = get_weather(
                    arguments["city"]
                )

            elif tool_name == "book_flight":

                result = book_flight(
                    arguments["destination"]
                )

            else:

                result = {
                    "error": f"Unknown tool: {tool_name}"
                }

            print("Tool result:", result)

            # Send tool result back to LLM
            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": json.dumps(result)
            })