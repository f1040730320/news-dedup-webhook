import os
import json
import requests
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def is_similar(new_text, existing_texts, threshold=0.9):
    if not existing_texts:
        return False
    vectorizer = TfidfVectorizer().fit_transform([new_text] + existing_texts)
    similarities = cosine_similarity(vectorizer[0:1], vectorizer[1:]).flatten()
    return any(score > threshold for score in similarities)

# 🧪 測試用：讀一筆新新聞 & 舊新聞
if __name__ == "__main__":
    # 新聞內容（模擬抓到的新資料）
    new_article = "Beijing is using a mix of carrots and sticks to try to prevent other countries from siding with the United States in isolating China."

    # 模擬從 Google Sheets 抓到的過去文章內容列表
    existing_articles = [
        "Beijing uses carrots and sticks to prevent countries from siding with the U.S. on isolating China.",
        "This is a completely different article with unrelated content."
    ]

    similar = is_similar(new_article, existing_articles)
    print("🔍 Is similar:", similar)
