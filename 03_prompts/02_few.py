# Few shot Prompting

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
api_key = os.getenv("GEMINI_API_KEY"),
base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# In few shot prompting, we provide the model with a few examples of the task we want it to perform. This helps the model understand the task better and generate more accurate responses.
SYSTEM_PROMPT = """
You are a helpful assistant that writes code. if the user asks you a question, you will answer it to the best of your ability. If you do not know the answer, you will say that you do not know.

Example 1:
Question: How is the weather today in Bengaluru?
Answer: Sorry , I can Help only Coding realated questions.

Example 2:
Question: Hey , Write a python function to add two numbers.
Answer: def add(x, y):
            return x + y
"""

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": "write a python function to add two numbers"
        }
    ]
)

print(response.choices[0].message.content)
