# model.py
def predict_sentiment(text: str) -> str:
    positive_words = ["happy", "great", "excellent", "good", "love", "amazing"]
    text_lower = text.lower()
    for word in positive_words:
        if word in text_lower:
            return "Positive"
    return "Negative"
