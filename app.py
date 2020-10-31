from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
import psycopg2
import os

app = Flask(__name__)
CORS(app)
DATABASE_URL = os.environ["DATABASE_URL"]

connection = psycopg2.connect(DATABASE_URL, sslmode="require")

@app.route('/recommendations/<int:user_id>', methods=["GET"])
@cross_origin()
def get_recommendations_by_user_id(user_id):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM recomendations;")
    
    result = cursor.fetchall()
    
    return jsonify([{"info1": row[1], "info2": row[2]} for row in result])



