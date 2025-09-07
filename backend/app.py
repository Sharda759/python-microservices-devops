from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/api/data")
def get_data():
    # Example data; you can connect to the database later
    return jsonify({
        "message": "Hello from the backend!",
        "status": "success"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
