from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return render_template("backend_page.html")


@app.route("/save_player", methods=['POST'])
def save_player():
    received_data = request.get_json()
    received_data = str(received_data)
    blob.upload_from_string(received_data)
    return jsonify({'message': 'Data received successfully'})


if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True)
