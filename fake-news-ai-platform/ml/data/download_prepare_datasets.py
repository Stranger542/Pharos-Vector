import os
import requests
import zipfile
import pandas as pd
from sklearn.model_selection import train_test_split

DATA_DIR = "ml/data"

def download_file(url, dest_path):
    if os.path.exists(dest_path):
        print(f"{dest_path} already exists, skipping.")
        return
    print(f"Downloading from {url}...")
    r = requests.get(url, stream=True)
    r.raise_for_status()
    with open(dest_path, "wb") as f:
        for chunk in r.iter_content(chunk_size=8192):
            f.write(chunk)
    print(f"Downloaded {dest_path}")

def unzip_file(zip_path, extract_to):
    if not os.path.exists(extract_to):
        os.makedirs(extract_to)
    with zipfile.ZipFile(zip_path, 'r') as z:
        z.extractall(extract_to)
    print(f"Extracted {zip_path}.")

def download_datasets():
    os.makedirs(DATA_DIR, exist_ok=True)
    # Download LIAR
    liar_zip = os.path.join(DATA_DIR, "liar_dataset.zip")
    download_file("https://www.cs.ucsb.edu/~william/data/liar_dataset.zip", liar_zip)
    unzip_file(liar_zip, DATA_DIR)

    # Download ISOT
    isot_zip = os.path.join(DATA_DIR, "isot_fake_news.zip")
    download_file("https://github.com/jmiranda27/FakeNewsNet/blob/master/dataset/isot/isot_fake_news.zip?raw=true", isot_zip)
    unzip_file(isot_zip, DATA_DIR)

def process_liar():
    liar_path = os.path.join(DATA_DIR, "LIAR", "liar_dataset", "train.tsv")
    liar_df = pd.read_csv(liar_path, sep="\t", header=None, names=[
        'id', 'label', 'statement', 'subject', 'speaker', 'job', 'state', 'party',
        'barely_true_counts', 'false_counts', 'pants_on_fire_counts', 'context'
    ])
    liar_df = liar_df[['statement', 'label']].dropna()
    liar_df['target'] = liar_df.label.apply(lambda x: 0 if x in ['true', 'mostly-true'] else 1)
    liar_final = liar_df[['statement', 'target']].rename(columns={'statement': 'text'})
    return liar_final

def process_isot():
    fake_path = os.path.join(DATA_DIR, "isot_fake_news", "Fake.csv")
    real_path = os.path.join(DATA_DIR, "isot_fake_news", "True.csv")
    fake_df = pd.read_csv(fake_path)[['title', 'text']].fillna('')
    real_df = pd.read_csv(real_path)[['title', 'text']].fillna('')
    fake_df['text'] = fake_df['title'] + ". " + fake_df['text']
    real_df['text'] = real_df['title'] + ". " + real_df['text']
    fake_df['target'] = 1
    real_df['target'] = 0
    isot_final = pd.concat([fake_df[['text', 'target']], real_df[['text', 'target']]])
    return isot_final

def create_splits():
    liar = process_liar()
    isot = process_isot()
    combined = pd.concat([liar, isot], ignore_index=True)
    combined = combined.dropna(subset=['text', 'target'])
    combined['target'] = combined['target'].astype(int)
    train_df, val_df = train_test_split(combined, test_size=0.1, random_state=42, stratify=combined['target'])
    train_df.to_csv(os.path.join(DATA_DIR, "train.csv"), index=False)
    val_df.to_csv(os.path.join(DATA_DIR, "val.csv"), index=False)
    print(f"Train set: {len(train_df)}, Validation set: {len(val_df)}")

if __name__ == "__main__":
    download_datasets()
    create_splits()
    print("All done!")