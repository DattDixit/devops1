# app.py
from flask import Flask, request, jsonify
from model import predict_sentiment

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>SproutsAI Sentiment Analysis API</h1><p>Use the /predict endpoint with a POST request.</p>"

@app.route("/predict", methods=['POST'])
def predict():
    """Endpoint to get sentiment predictions."""
    if not request.json or 'text' not in request.json:
        return jsonify({"error": "Missing 'text' in request body"}), 400

    text_to_analyze = request.json['text']
    sentiment = predict_sentiment(text_to_analyze)

    response = {
        "text": text_to_analyze,
        "sentiment": sentiment
    }
    return jsonify(response)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
