from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.models.bert_fake_news_classifier import BertFakeNewsClassifier

router = APIRouter()

class ArticleInput(BaseModel):
    text: str

class PredictionResponse(BaseModel):
    label: str
    score: float

bert_classifier = BertFakeNewsClassifier()

@router.post("/predict", response_model=PredictionResponse)
def predict_fake_news(article: ArticleInput):
    preds, scores = bert_classifier.predict([article.text])
    label = "fake" if preds[0] == 1 else "real"
    score = scores[0][preds[0]]
    return PredictionResponse(label=label, score=float(score))
