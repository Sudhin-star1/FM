# Sentiment Analysis API 🚀

A simple FastAPI microservice that performs sentiment analysis using HuggingFace transformers.

## How to Run

### Locally:
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### With Docker:
```bash
docker build -t sentiment-api .
docker run -p 8000:8000 sentiment-api
```

### Docker Compose:
```bash
docker-compose up --build
```

## Endpoints
- `GET /` — Health check
- `POST /analyze` — Analyze text for sentiment

```json
{
  "text": "I love this product!"
}
```

## Tests
```bash
pytest
```

## CI/CD
- GitHub Actions runs tests on push/pull requests

## License
MIT