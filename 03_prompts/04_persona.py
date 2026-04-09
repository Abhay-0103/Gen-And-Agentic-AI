# Persona Based Prompting

import os
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

SYSTEM_PROMPT = """
    You are an AI Persona Assistant named Abhay Singh.
    You are acting on behalf of Abhay Singh who is 22 years old Tech enthusiast and principle engineer. Your main tech stack is JS and Python and DSA only in Java and you are learning GeAI these days.

    Example:
    Q: Hey
    A: Kaho , Lowdu ka haal ba sab thik!
"""


response = client.chat.completions.create(
        model="gemini-2.5-flash",
        messages=[
            {
                "role" : "system",
                "content" : SYSTEM_PROMPT
            },
            {
                "role" : "user",
                "content" : "Hey There"
            }
        ]
    )

print("Response:", response.choices[0].message.content)