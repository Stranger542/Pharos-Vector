import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle

df_liar = pd.read_csv("ml/data/LIAR/liar_dataset/train.tsv", sep="\t", header=None, names=[
    'id', 'label', 'statement', 'subject', 'speaker', 'job', 'state', 'party',
    'barely_true_counts', 'false_counts', 'pants_on_fire_counts', 'context'
])
texts = df_liar['statement'].dropna().tolist()

vectorizer = TfidfVectorizer(max_features=10000, ngram_range=(1,2))
vectorizer.fit(texts)

with open("ml/vectorizer/tfidf_vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)
