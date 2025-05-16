from transformers import pipeline
from app.config import settings

sentiment_pipeline = pipeline("sentiment-analysis", model=settings.model_name)

def analyze_sentiment(text: str):
    result = sentiment_pipeline(text)[0]
    return {
        "label": result["label"].lower(),
        "score": round(result["score"], 4)
    }
    