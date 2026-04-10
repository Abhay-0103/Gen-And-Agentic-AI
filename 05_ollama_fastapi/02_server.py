from fastapi import FastAPI, Body
from ollama import Client

app = FastAPI()

client = Client(
    host="http://localhost:11434",
)

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/contact-us")
def contact_us():
    return {"message": "Contact us at 123-456-7890"}

@app.post("/chat")
def chat(message: str = Body(...)):
    response = client.chat(
        model="gemma:2b",
        messages=[
            {
                "role": "user",
                "content": message,
            }
        ]
    )

    return {
        "response": response["message"]["content"]
    }