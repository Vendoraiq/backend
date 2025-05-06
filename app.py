from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return 'VendorAIQ Backend is live!'

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    asin = data.get('asin')

    return jsonify({
        "title": "Sample Product Title",
        "asin": asin,
        "roi": 85,
        "buy_box": 27.99,
        "est_sales": 150,
        "supplier_name": "Seoul4PM",
        "image": "https://via.placeholder.com/150"
    })

if __name__ == '__main__':
    app.run(debug=True)
