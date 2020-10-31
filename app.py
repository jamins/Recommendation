from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)
DB_URL = "postgres://aqutuzrfdzsdeg:fecd7ec0c96cd4494dc1a99334a6bfef46ce26fd7906cfe341d5925994b2a989@ec2-54-217-204-34.eu-west-1.compute.amazonaws.com:5432/dcteppef0ebqt9"

connection = psycopg2.connect(DATABASE_URL, sslmode="require")

@app.route('/recommendations/<int: user_id>', methods=["GET"])
def get_recommendations_by_user_id(user_id):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM recomendations;")
    
    result = cursor.fetchall()
    
    return jsonify([{"info1": row["INFO1"], "info2": row["INFO2"] from row in result}])
