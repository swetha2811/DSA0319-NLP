from textblob import TextBlob
sentences = [
    "I love this product! It's amazing.",
    "The weather is terrible today."
]
for sentence in sentences:
    blob = TextBlob(sentence)
    sentiment_score = blob.sentiment.polarity
    if sentiment_score > 0:
        sentiment = "positive"
    elif sentiment_score < 0:
        sentiment = "negative"
    else:
        sentiment = "neutral"
    print(f"Sentence: '{sentence}'")
    print(f"Sentiment: {sentiment} (Polarity score: {sentiment_score})")
    print()
