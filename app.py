from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow frontend requests

@app.route("/")
def home():
    return "VendorAIQ Backend is Running."

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    asin = data.get("asin")

    # Simulated example result – replace this with real logic later
    return jsonify({
        "title": "Sample Product Title",
        "asin": asin,
        "roi": 35.6,
        "buy_box": 23.99,
        "est_sales": 140,
        "supplier_name": "Seoul4PM",
        "image": "https://via.placeholder.com/200"
    })

if __name__ == "__main__":
    app.run()
