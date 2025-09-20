import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_fake_news_predict_real():
    response = client.post("/api/v1/fake-news/predict", json={"text": "The sky is blue."})
    assert response.status_code == 200
    json_data = response.json()
    assert "label" in json_data
    assert json_data["label"] in ["real", "fake"]

def test_source_credibility():
    response = client.post("/api/v1/source/credibility", json={"domain": "bbc.com"})
    assert response.status_code == 200
    json_data = response.json()
    assert "trust_score" in json_data

def test_claim_verification():
    response = client.post("/api/v1/claims/verify", json={"claim": "The earth is flat."})
    assert response.status_code == 200
    json_data = response.json()
    assert "checks" in json_data
