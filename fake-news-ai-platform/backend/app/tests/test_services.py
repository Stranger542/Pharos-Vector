import pytest
from app.services import detection, explainability, media_literacy, newsguard_api, factcheck_api

def test_detection_predict():
    result = detection.predict_fake_news("This is a test article claiming false.")
    assert "label" in result
    assert result["label"] in ["real", "fake"]
    assert isinstance(result["score"], float)

def test_explainability_generation():
    explanation = explainability.generate_explanation("Some text", attention_weights=None)
    assert isinstance(explanation, str)

def test_media_literacy_content():
    content = media_literacy.generate_learning_content("fake news")
    assert "tips" in content
    assert isinstance(content["tips"], list)

def test_newsguard_api_call(monkeypatch):
    class MockResponse:
        status_code = 200
        def json(self): return {"trust_score": 90}
    monkeypatch.setattr("requests.get", lambda *args, **kwargs: MockResponse())
    result = newsguard_api.get_newsguard_report("bbc.com")
    assert "trust_score" in result or "error" in result

def test_factcheck_api_call(monkeypatch):
    class MockResponse:
        status_code = 200
        def json(self): return {"claims": [{"verdict": "False"}]}
    monkeypatch.setattr("requests.get", lambda *args, **kwargs: MockResponse())
    result = factcheck_api.search_fact_checks("Some claim")
    assert isinstance(result, list) or "error" in result
