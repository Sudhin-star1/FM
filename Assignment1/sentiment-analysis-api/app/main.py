from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.utils import analyze_sentiment

app = FastAPI(title="Sentiment Analysis API")

class TextInput(BaseModel):
    text: str

@app.get("/")
def read_root():
    return {"message": "Sentiment Analysis API is running!"}

@app.post("/analyze")
def analyze(input: TextInput):
    if not input.text.strip():
        raise HTTPException(status_code=400, detail="Text input is empty")
    return analyze_sentiment(input.text)
