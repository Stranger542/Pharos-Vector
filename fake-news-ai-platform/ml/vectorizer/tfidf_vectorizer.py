import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle

df_liar = pd.read_csv("ml/data/liar_train.csv")

texts = df_liar.get('statement', df_liar.get('text')).dropna().tolist()

vectorizer = TfidfVectorizer(max_features=10000, ngram_range=(1,2))
vectorizer.fit(texts)

with open("ml/vectorizer/tfidf_vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)
