from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
#import psycopg2
#import os
from recsys import predict


app = Flask(__name__)
CORS(app)
#DATABASE_URL = os.environ["DATABASE_URL"]

#connection = psycopg2.connect(DATABASE_URL, sslmode="require")

"""@app.route('/test-recommendations/books')
@cross_origin()
def get_books_recommendations():
    test_data = [[ 38487,  39908],
        [  1711, 128165],
        [106958, 317628],
        [ 98101, 379271]]
    return jsonify(predict(test_data).tolist())
"""

@app.route('/recommendations/<int:user_id>', methods=["GET"])
@cross_origin()
def get_recommendations_by_user_id(user_id):
#    cursor = connection.cursor()
#    cursor.execute("SELECT * FROM recomendations;")
    
#    result = cursor.fetchall()
    
    return jsonify([
        {
            "author": [
                "Пушкин",
                "Пушкин"
            ],
            "name": "Книга про пейзан деревенских",
            "city": [
                 "Москва",
                 "Питеор"
            ],
            "publisher": "АСТ",
            "year": "1988",
            "book": "Серия книг про пейзан от пушкина",
            "theme": [
                "Деревня ебаная",
                "Пейзане"
            ],
            "knowlage_id": 1,
            "age_rating": 18
        },
        {
            "author": [
                "Пушкин",
                "Лермонтов"
            ],
            "name": "Сборник стихов",
            "city": [
                 "Москва",
                 "Питеор"
            ],
            "publisher": "АСТ",
            "year": "2005",
            "book": "Сборники стихов",
            "theme": [
                "Стихи",
                "Поеты"
            ],
            "knowlage_id": 1,
            "age_rating": 18
        },
        {
            "author": [
                "А. П. Чехов"
            ],
            "name": "Вишнёвый сад",
            "city": [
                 "Москва",
                 "Питеор"
            ],
            "publisher": "АСТ",
            "year": "2005",
            "book": "Сборники стихов",
            "theme": [
                "Куколды",
                "Майнкрафт"
            ],
            "knowlage_id": 1,
            "age_rating": 16
        }
    ])



#app.run()
