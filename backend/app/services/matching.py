from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
import numpy as np

# Load model (lazy load pattern preferable in production, but global for simplicity here)
model = SentenceTransformer('all-MiniLM-L6-v2')

def calculate_tfidf_similarity(text1: str, text2: str) -> float:
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform([text1, text2])
    return cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0] * 100

def calculate_semantic_similarity(text1: str, text2: str) -> float:
    embeddings = model.encode([text1, text2])
    similarity = cosine_similarity([embeddings[0]], [embeddings[1]])[0][0]
    return similarity * 100

def match_resume_to_job(resume_text: str, job_description: str) -> dict:
    tfidf_score = calculate_tfidf_similarity(resume_text, job_description)
    semantic_score = calculate_semantic_similarity(resume_text, job_description)
    
    # Weighted average: 40% TF-IDF (Keywords), 60% Semantic (Context)
    final_score = (tfidf_score * 0.4) + (semantic_score * 0.6)
    
    return {
        "overall_score": round(final_score, 1),
        "keyword_match": round(tfidf_score, 1),
        "semantic_match": round(semantic_score, 1)
    }
