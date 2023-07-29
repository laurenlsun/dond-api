from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import os
from google.cloud import storage


app = Flask(__name__)
CORS(app)

# Initialize the client
client = storage.Client()
# Get the bucket
bucket = client.get_bucket('dond-b.online')
# Create or get the file in the bucket
blob = bucket.blob('data.txt')


@app.route("/")
def home():
    return render_template("backend_page.html")


@app.route("/save_player", methods=['POST'])
def save_player():
    received_data = request.get_json()
    received_data = str(received_data)
    if blob is not None:
        prior_data = blob.download_as_text()
        new_data = prior_data + "\n" + received_data # append received data string
        blob.upload_from_string(new_data)
        return jsonify({'message': 'Data received and saved successfully'})


if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True)
