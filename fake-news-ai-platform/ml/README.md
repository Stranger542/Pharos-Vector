# Fake News Detection ML Pipeline

## Workflow

1. **Data Download and Preparation:**
   - Run `python ml/data/download_prepare_datasets.py`
   - Downloads LIAR & ISOT datasets, prepares train/val splits.

2. **Training:**
   - Run `python ml/training/train_bert.py`
   - Trains BERT model only on GPU, saves `bert_fakenews.pt`.

3. **Evaluation:**
   - Run `python ml/evaluation/eval_bert.py`
   - Evaluates the model, prints metrics, saves confusion matrix to PNG.

4. **Inference:**
   - Use `models/bert_fake_news_classifier.py` class for easy API/production integration.

5. **Optional TF-IDF Baseline:**
   - Run `python ml/vectorizer/tfidf_vectorizer.py` for classic vectorizer.

## Data

- LIAR and ISOT datasets managed and split automatically.
- No manual dataset download required.
- Files: `train.csv`, `val.csv` are generated automatically.

## Requirements

- Python 3.8+
- CUDA-enabled GPU required for training/evaluation
- Dependencies: `transformers`, `torch`, `pandas`, `scikit-learn`, `matplotlib`, `seaborn`, `requests`

## Structure
See main project README for overall structure and usage.
