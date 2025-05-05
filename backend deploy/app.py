from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "VendorAIQ backend is running!"

@app.route("/api/test", methods=["GET"])
def test():
    return jsonify({"status": "success", "message": "API is working!"})

if __name__ == "__main__":
    app.run(debug=True)