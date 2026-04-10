# Chain of Thought (CoT) Prompting - Multi Task AI (Continuous Chat Mode)

import os
import json
import requests
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

# Initialize client
client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# -------------------- TOOL -------------------- #
def get_weather(city: str):
    try:
        url = f"https://wttr.in/{city.lower()}?format=%C+%t"
        response = requests.get(url)

        if response.status_code == 200:
            return f"The current weather in {city} is: {response.text}"
        return "Failed to fetch weather data."

    except Exception as e:
        return f"Error: {str(e)}"


available_tools = {
    "get_weather": get_weather
}

# -------------------- SYSTEM PROMPT -------------------- #
SYSTEM_PROMPT = """
You are an AI assistant that MUST respond in JSON format.

Format:
{
  "step": "START | PLAN | TOOL | OUTPUT",
  "content": "your response",
  "tool_name": "optional",
  "tool_input": "optional"
}

Rules:
1. Always return valid JSON.
2. Follow order: START → PLAN → TOOL (if needed) → OUTPUT.
3. No extra text outside JSON.

Tasks:
- Math → step-by-step solution
- Coding → clean code + explanation
- Motivation → practical advice
- Weather → MUST call tool
"""

print("\n🚀 AI Chat Started (type 'exit' to quit)\n")

# Keep system prompt persistent
message_history = [
    {"role": "system", "content": SYSTEM_PROMPT}
]

# -------------------- CHAT LOOP -------------------- #
while True:

    user_query = input("🧑 You: ")

    if user_query.lower() in ["exit", "quit"]:
        print("\n👋 Exiting... Bye!")
        break

    message_history.append({
        "role": "user",
        "content": user_query
    })

    # Inner CoT loop
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

        # -------- HANDLE STEPS -------- #

        if step == "START":
            print("🔹 START:", content)

        elif step == "PLAN":
            print("🧠 PLAN:", content)

        elif step == "TOOL":
            tool_name = parsed_result.get("tool_name")
            tool_input = parsed_result.get("tool_input")

            print(f"🛠️ TOOL CALL: {tool_name}({tool_input})")

            if tool_name in available_tools:
                result = available_tools[tool_name](tool_input)

                message_history.append({
                    "role": "assistant",
                    "content": raw_result
                })

                message_history.append({
                    "role": "user",
                    "content": f"Tool result: {result}"
                })

                continue
            else:
                print("❌ Tool not found")
                break

        elif step == "OUTPUT":
            print("🤖 AI:", content)

            message_history.append({
                "role": "assistant",
                "content": raw_result
            })

            break  # break inner loop ONLY

        else:
            print("❌ Unknown step:", step)
            break

print("\n✅ Session Ended\n")