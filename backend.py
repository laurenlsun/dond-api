from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv
import psycopg2 as ps

app = Flask(__name__)
CORS(app)

load_dotenv()
db_host = os.getenv("YOUR_GOOGLE_CLOUD_PUBLIC_IP")
db_user = os.getenv("YOUR_DATABASE_USERNAME")
db_pass = os.getenv("YOUR_DATABASE_PASSWORD")
db_name = os.getenv("YOUR_DATABASE_NAME")


@app.route("/")
def home():
    return render_template("backend_page.html")


@app.route("/save_player", methods=['POST'])
def save_player():
    received_data = request.get_json()
    save_to_psql(received_data)
    return jsonify({'message': 'Data received successfully'})


def save_to_psql(data):
    conn = ps.connect(host=db_host,
        user=db_user,
        password=db_pass,
        database=db_name)
    cursor = conn.cursor()

    cursor.execute("INSERT INTO games (game_id, player_id, game_mode, end_result, stop_round, winnings) \
             VALUES (11114, 10114, 0, 'TEST', 0, 0);")

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True)
