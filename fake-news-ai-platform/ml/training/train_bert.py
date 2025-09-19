import torch
from torch.utils.data import DataLoader, Dataset
from transformers import BertTokenizer, BertForSequenceClassification, AdamW, get_linear_schedule_with_warmup
import pandas as pd
import numpy as np
import os

DATA_DIR = "ml/data"
MODEL_DIR = "ml/models"
EPOCHS = 3
BATCH_SIZE = 32
MAX_LEN = 256

assert torch.cuda.is_available(), "CUDA is required for training!"

class NewsDataset(Dataset):
    def __init__(self, texts, labels, tokenizer, max_len):
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
    train_df = pd.read_csv(f"{DATA_DIR}/train.csv")
    tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
    train_dataset = NewsDataset(train_df['text'].tolist(), train_df['target'].values, tokenizer, MAX_LEN)
    train_loader = DataLoader(train_dataset, batch_size=BATCH_SIZE, shuffle=True)

    device = torch.device("cuda")
    model = BertForSequenceClassification.from_pretrained("bert-base-uncased", num_labels=2).to(device)
    optimizer = AdamW(model.parameters(), lr=2e-5)
    scheduler = get_linear_schedule_with_warmup(optimizer, 100, len(train_loader) * EPOCHS)

    for epoch in range(EPOCHS):
        model.train()
        losses = []
        for batch in train_loader:
            batch = {k: v.to(device) for k, v in batch.items()}
            loss = model(**batch).loss
            loss.backward()
            optimizer.step()
            scheduler.step()
            optimizer.zero_grad()
            losses.append(loss.item())
        print(f"Epoch {epoch+1} loss: {np.mean(losses):.4f}")

    os.makedirs(MODEL_DIR, exist_ok=True)
    torch.save(model.state_dict(), f"{MODEL_DIR}/bert_fakenews.pt")
    print("Training complete! Model saved to ml/models/bert_fakenews.pt.")

if __name__ == "__main__":
    main()
