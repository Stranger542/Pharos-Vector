# API Documentation

## Base URL

`/api/v1`

## Endpoints

### Fake News Prediction

- `POST /fake-news/predict`
- Request Body: `{ "text": "article text here" }`
- Response: `{ "label": "fake" | "real", "score": float }`

### Source Credibility

- `POST /source/credibility`
- Request Body: `{ "domain": "example.com" }`
- Response: `{ "domain": string, "trust_score": int, "summary": string }`

### Fact-Check Claims

- `POST /claims/verify`
- Request Body: `{ "claim": "text" }`
- Response: `{ "claim": string, "checks": [...] }`

### Media Literacy

- `POST /learning/deconstruct`
- Request Body: `{ "topic": "topic string" }`
- Response: `{ "questions": [...] }`

### User Profile

- `POST /user/profile`
- Request Body: `{ "username": "string" }`
- Response: `{ "username": string, "saved_articles": [...], "quiz_stats": {...} }`
