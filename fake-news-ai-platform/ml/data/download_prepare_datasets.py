import os
import requests
import zipfile
import pandas as pd
from sklearn.model_selection import train_test_split
import sys
import kagglehub

# Directory to store all datasets
DATA_DIR = "ml/data"

def download_file(url, dest_path):
    """Downloads a file from a URL, streaming to handle large files."""
    if os.path.exists(dest_path):
        print(f"'{os.path.basename(dest_path)}' already exists, skipping download.")
        return
    print(f"Downloading from {url}...")
    try:
        r = requests.get(url, stream=True)
        r.raise_for_status()
        with open(dest_path, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"Successfully downloaded '{os.path.basename(dest_path)}'")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading {url}: {e}")
        sys.exit(1)


def unzip_file(zip_path, extract_to):
    """Unzips a file to a specified directory."""
    if not os.path.exists(extract_to):
        print(f"Creating directory '{extract_to}'")
        os.makedirs(extract_to)
    try:
        with zipfile.ZipFile(zip_path, 'r') as z:
            z.extractall(extract_to)
        print(f"Successfully extracted '{os.path.basename(zip_path)}'.")
    except zipfile.BadZipFile:
        print(f"Error: The file '{os.path.basename(zip_path)}' is not a zip file or is corrupted.")
        sys.exit(1)


def download_and_check_datasets():
    """Manages the download and verification of required datasets."""
    os.makedirs(DATA_DIR, exist_ok=True)
    
    # --- LIAR Dataset Check (manual) ---
    liar_dir = os.path.join(DATA_DIR, "liar-dataset")
    liar_train_path = os.path.join(liar_dir, "train.tsv")
    if not os.path.exists(liar_train_path):
        print("🛑 LIAR dataset not found!")
        print("Please download the dataset from: https://www.kaggle.com/datasets/doanquanvietnamca/liar-dataset")
        print(f"Then, unzip it and place the contents in the '{liar_dir}' directory.")
        sys.exit(1)
    print("✅ LIAR dataset found.")

    # --- ISOT Dataset Download (auto) ---
    isot_extract_path = kagglehub.dataset_download("clmentbisaillon/fake-and-real-news-dataset")
    print(f"✅ ISOT dataset downloaded to: {isot_extract_path}")
    return isot_extract_path


def process_liar():
    """Reads, combines, and processes the LIAR dataset (train, valid, test)."""
    print("Processing LIAR dataset...")
    base_path = os.path.join(DATA_DIR, "liar-dataset")
    paths = {
        "train": os.path.join(base_path, "train.tsv"),
        "val": os.path.join(base_path, "valid.tsv"),
        "test": os.path.join(base_path, "test.tsv")
    }

    column_names = [
        'id', 'label', 'statement', 'subject', 'speaker', 'job', 'state', 'party',
        'barely_true_counts', 'false_counts', 'half_true_counts',
        'mostly_true_counts', 'pants_on_fire_counts', 'context'
    ]
    
    df_list = [pd.read_csv(p, sep="\t", header=None, names=column_names) for p in paths.values()]
    liar_df = pd.concat(df_list, ignore_index=True)

    liar_df = liar_df[['statement', 'label']].dropna()
    liar_df['target'] = liar_df['label'].apply(lambda x: 0 if x in ['true', 'mostly-true'] else 1)
    liar_final = liar_df[['statement', 'target']].rename(columns={'statement': 'text'})
    print(f"Processed {len(liar_final)} entries from LIAR dataset.")
    return liar_final


def process_isot(isot_extract_path):
    """Reads and processes the ISOT Fake News dataset."""
    print("Processing ISOT dataset...")
    fake_path = os.path.join(isot_extract_path, "Fake.csv")
    real_path = os.path.join(isot_extract_path, "True.csv")
    
    fake_df = pd.read_csv(fake_path)
    real_df = pd.read_csv(real_path)

    fake_df['text'] = fake_df['title'].fillna('') + ". " + fake_df['text'].fillna('')
    real_df['text'] = real_df['title'].fillna('') + ". " + real_df['text'].fillna('')
    
    fake_df['target'] = 1  # Fake news
    real_df['target'] = 0  # Real news
    
    isot_final = pd.concat([
        fake_df[['text', 'target']],
        real_df[['text', 'target']]
    ], ignore_index=True)
    print(f"Processed {len(isot_final)} entries from ISOT dataset.")
    return isot_final


def create_splits(isot_extract_path):
    """Combines datasets and creates final training and validation CSV files."""
    print("Combining datasets and creating final splits...")
    liar = process_liar()
    isot = process_isot(isot_extract_path)
    
    combined = pd.concat([liar, isot], ignore_index=True)
    combined = combined.dropna(subset=['text'])
    combined['text'] = combined['text'].astype(str)
    combined = combined[combined['text'].str.strip() != '']
    combined['target'] = combined['target'].astype(int)

    train_df, val_df = train_test_split(
        combined,
        test_size=0.1,
        random_state=42,
        stratify=combined['target']
    )
    
    train_path = os.path.join(DATA_DIR, "train.csv")
    val_path = os.path.join(DATA_DIR, "val.csv")
    
    train_df.to_csv(train_path, index=False)
    val_df.to_csv(val_path, index=False)
    
    print("\n--- Data Preparation Complete ---")
    print(f"Total combined entries: {len(combined)}")
    print(f"Training set size: {len(train_df)}")
    print(f"Validation set size: {len(val_df)}")
    print(f"Train/Val splits saved to '{DATA_DIR}'")
    print("---------------------------------")


if __name__ == "__main__":
    isot_extract_path = download_and_check_datasets()
    create_splits(isot_extract_path)
