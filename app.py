from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)
DATABASE_URL = os.environ["DATABASE_URL"]

connection = psycopg2.connect(DATABASE_URL, sslmode="require")

@app.route('/recommendations/<int:user_id>', methods=["GET"])
def get_recommendations_by_user_id(user_id):
#    cursor = connection.cursor()
#    cursor.execute("SELECT * FROM recomendations;")
    
#    result = cursor.fetchall()
    
    return "Sukaah (" #jsonify([{"info1": row["INFO1"], "info2": row["INFO2"]} for row in result])



