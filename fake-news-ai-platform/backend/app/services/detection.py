import threading
from app.models.bert_fake_news_classifier import BertFakeNewsClassifier

_model = None
_model_lock = threading.Lock()

def get_bert_classifier():
    global _model
    if _model is None:
        with _model_lock:
            if _model is None:
                _model = BertFakeNewsClassifier()
    return _model

def predict_fake_news(text: str):
    model = get_bert_classifier()
    preds, scores = model.predict([text])
    return {"label": "fake" if preds[0] == 1 else "real", "score": float(scores[0][preds[0]])}
