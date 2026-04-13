from dotenv import load_dotenv
from mem0 import Memory
import os
from openai import OpenAI

load_dotenv()

client = OpenAI()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

config = {
    "version": "v1.1",
    "embedder": {
        "provider": "openai",
        "config": {
            "api_key": OPENAI_API_KEY,
            "model": "text-embedding-3-small"
        }
    },
    "llm": {
        "provider": "openai",
        "config": {
            "api_key": OPENAI_API_KEY,
            "model": "gemini-2.5-flash"
        }
    },
    "vector_store": {
        "provider": "qdrant",
        "config": {
            "host": "localhost",
            "port": 6333,
        }
    }
}

mem_client = Memory.from_config(config)


user_query = input("> Kuch Bol BSDK: ")

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {
            "role": "user",
            "content": user_query
        }
    ]
)

ai_response = response.choices[0].message.content

print(f"AI:", ai_response)

mem_client.add(
    user_id="abhay_0103",
    messages=[
        {
            "role": "user",
            "content": user_query
        },
        {
            "role": "assistant",
            "content": ai_response
        }
    ]
)

print("Memory added successfully!")