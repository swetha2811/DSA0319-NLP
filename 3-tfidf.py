from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
documents = [
    "Artificial intelligence (Al) is a field of computer science.",
    "Machine learning is a subset of Al that focuses on training models to makepredictions.",
    "Deep learning is a type of machine learning that uses neural networks with multiple layers.",
    "Neural networks are composed of interconnected nodes called neurons.",
    "Recurrent neural networks (RNNs) are commonly used in natural language processing tasks."]
query = "TF-IDF in information retrieval"
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(documents + [query])
cosine_similarities = linear_kernel(tfidf_matrix[-1], tfidf_matrix[:-1])
                                                            .flatten()
document_ranking = sorted(enumerate(cosine_similarities), key=lambda
                          x:x[1], reverse=True)
print("Ranked Documents:")
for i, similarity in document_ranking:
    print(f"Document {i + 1}: Similarity = {similarity:.4f}")
    print(f"   {documents[i]}")
    print()
