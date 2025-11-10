from google import genai
from fastapi import FastAPI

client = genai.Client()

app = FastAPI()

@app.get("/chat")
async def chat():
    response = client.models.generate_content(
        model="gemini-2.5-flash", contents="Explain how AI works in a few words")
    return response.text
