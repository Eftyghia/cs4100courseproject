import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class BookSearchEngine:
    def __init__(self, summaries):
        self.vectorizer = TfidfVectorizer(stop_words="english")
        self.tfidf = self.vectorizer.fit_transform(summaries["summary"])
        self.summaries = summaries

    def search(self, query, k=5):
        q_vec = self.vectorizer.transform([query])
        scores = cosine_similarity(q_vec, self.tfidf)[0]
        topk = scores.argsort()[::-1][:k]
        return self.summaries.iloc[topk], scores[topk]
