# Zero Shot Prompting

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
api_key = os.getenv("GEMINI_API_KEY"),
base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# In zero shot prompting, we do not provide any examples to the model. We simply ask it to perform a task based on the instructions we give it.
SYSTEM_PROMPT = "You are a helpful assistant that writes code. if the user asks you a question, you will answer it to the best of your ability. If you do not know the answer, you will say that you do not know."

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": "How is the weather today in Bengaluru?"
        }
    ]
)

print(response.choices[0].message.content)
