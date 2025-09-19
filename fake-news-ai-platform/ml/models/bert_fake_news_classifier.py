import torch
from transformers import BertTokenizer, BertForSequenceClassification

class BertFakeNewsClassifier:
    def __init__(self, model_weights="ml/models/bert_fakenews.pt", num_labels=2):
        self.device = torch.device("cuda")
        self.model = BertForSequenceClassification.from_pretrained("bert-base-uncased", num_labels=num_labels)
        self.model.load_state_dict(torch.load(model_weights, map_location=self.device))
        self.model.to(self.device)
        self.model.eval()
        self.tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")

    def predict(self, texts):
        encodings = self.tokenizer(texts, truncation=True, padding=True, max_length=256, return_tensors="pt")
        encodings = {k: v.to(self.device) for k, v in encodings.items()}
        with torch.no_grad():
            outputs = self.model(**encodings)
            probs = torch.softmax(outputs.logits, dim=-1)
            preds = torch.argmax(probs, dim=-1)
        return preds.cpu().tolist(), probs.cpu().tolist()
