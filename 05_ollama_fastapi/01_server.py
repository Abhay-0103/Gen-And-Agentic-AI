from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/contact-us")
def contact_us():
    return {"message": "Contact us at 123-456-7890"}