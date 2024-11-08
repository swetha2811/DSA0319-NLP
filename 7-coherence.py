from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.tokenize import sent_tokenize, word_tokenize
sample_text = """
once upon a time, there was a young boy named peter.
he lived in a small village.
one day, he decided to explore the nearby forest.
"""
sentences = sent_tokenize(sample_text)
tfidf_matrix = TfidfVectorizer().fit_transform(sentences)
coherence_scores = cosine_similarity(tfidf_matrix[:-1], tfidf_matrix[1:]).flatten()
average_coherence = sum(coherence_scores) / len(coherence_scores)
print("Coherence of the provided text:", average_coherence)
