# Chain of Thought (CoT) Prompting Example

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
You are an AI assistant that MUST respond in JSON format.

Format:
{
  "step": "START | PLAN | OUTPUT",
  "content": "your response"
}

Rules:
1. Always respond in valid JSON.
2. Follow order: START → PLAN → OUTPUT.
3. No extra text outside JSON.
"""

print("\n\n\n")

message_history = [
    {"role": "system", "content": SYSTEM_PROMPT}
]

user_query = input("Enter your query: ")

message_history.append({
    "role": "user",
    "content": user_query
})

while True:
    response = client.chat.completions.create(
        model="gemini-2.5-flash",
        response_format={"type": "json_object"},
        messages=message_history
    )

    raw_result = response.choices[0].message.content

    try:
        parsed_result = json.loads(raw_result)
    except json.JSONDecodeError:
        print("❌ Invalid JSON:", raw_result)
        break

    step = parsed_result.get("step", "").upper()
    content = parsed_result.get("content", "")

    if step == "START":
        print("🔹 START:", content)

    elif step == "PLAN":
        print("🧠 PLAN:", content)

    elif step == "OUTPUT":
        print("✅ OUTPUT:", content)
        break

    message_history.append({
        "role": "assistant",
        "content": raw_result
    })

print("\n\n\n")