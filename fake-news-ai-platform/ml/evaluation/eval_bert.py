import torch
from torch.utils.data import DataLoader, Dataset
from transformers import BertTokenizer, BertForSequenceClassification
from sklearn.metrics import accuracy_score, f1_score, classification_report, confusion_matrix
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

DATA_DIR = "ml/data"
MODEL_DIR = "ml/models"

class NewsDataset(Dataset):
    def __init__(self, texts, labels, tokenizer, max_len=256):
        self.texts = texts
        self.labels = labels
        self.tokenizer = tokenizer
        self.max_len = max_len
    def __len__(self):
        return len(self.texts)
    def __getitem__(self, idx):
        enc = self.tokenizer(self.texts[idx], truncation=True, padding='max_length', max_length=self.max_len, return_tensors="pt")
        item = {k: v.squeeze(0) for k, v in enc.items()}
        item['labels'] = torch.tensor(self.labels[idx], dtype=torch.long)
        return item

def main():
    val_df = pd.read_csv(f"{DATA_DIR}/val.csv")
    tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
    val_dataset = NewsDataset(val_df['text'].tolist(), val_df['target'].values, tokenizer)
    val_loader = DataLoader(val_dataset, batch_size=32)
    device = torch.device("cuda")
    model = BertForSequenceClassification.from_pretrained("bert-base-uncased", num_labels=2)
    model.load_state_dict(torch.load(f"{MODEL_DIR}/bert_fakenews.pt", map_location=device))
    model.to(device)
    model.eval()

    all_labels, all_preds = [], []
    for batch in val_loader:
        batch = {k: v.to(device) for k, v in batch.items()}
        with torch.no_grad():
            logits = model(**batch).logits
            preds = torch.argmax(logits, dim=-1).cpu().numpy()
            labels = batch['labels'].cpu().numpy()
            all_labels.extend(labels)
            all_preds.extend(preds)

    print("Accuracy:", accuracy_score(all_labels, all_preds))
    print("F1 Score:", f1_score(all_labels, all_preds))
    print(classification_report(all_labels, all_preds))
    cm = confusion_matrix(all_labels, all_preds)
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Real', 'Fake'], yticklabels=['Real', 'Fake'])
    plt.xlabel("Predicted")
    plt.ylabel("True")
    plt.title("Confusion Matrix BERT Fake News")
    plt.savefig("ml/evaluation/confusion_matrix.png")
    print("Confusion matrix saved.")

if __name__ == "__main__":
    main()
