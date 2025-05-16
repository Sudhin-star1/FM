from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Sentiment Analysis API is running!"}

def test_analyze():
    response = client.post("/analyze", json={"text": "I love this!"})
    assert response.status_code == 200
    assert "label" in response.json()
    assert response.json()["label"] in ["positive", "neutral", "negative"]