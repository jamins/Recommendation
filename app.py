from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
import psycopg2
import os
from recsys import predict_book #, predict_clf


app = Flask(__name__)
CORS(app)
DATABASE_URL = os.environ["DATABASE_URL"]

connection = psycopg2.connect(DATABASE_URL, sslmode="require")


@app.route('/recommendations/books/<int:user_id>', methods=["GET"])
@cross_origin()
def get_book_recommendations_by_user_id(user_id):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM books;")
    
    result = cursor.fetchall()
    test_data = [[user_id, row[0]] for row in result]
    predicted_list = predict_book(test_data).tolist() 
    predicted_list = [[predicted[0], test[1]] for (test, predicted) in zip(test_data, predicted_list)]
    
    predicted_list = sorted(predicted_list, key=lambda x: x[0] ,reverse=True)
    predicted_list = predicted_list[:20]
    
    responce = []
    for predicted in predicted_list:
        
        cursor.execute("SELECT * FROM books WHERE ID =" + str(predicted[1]))
        book_data = cursor.fetchall()
        cursor.execute("SELECT authors.ID, authors.NAME FROM books_authors LEFT JOIN authors ON authors.ID = books_authors.AUTHOR_ID WHERE BOOK_ID =" + str(predicted[1]))
        author_data = cursor.fetchall()
        cursor.execute("SELECT themes.ID, themes.NAME FROM books_themes LEFT JOIN themes ON themes.ID = books_themes.THEME_ID WHERE BOOK_ID =" + str(predicted[1]))
        theme_data = cursor.fetchall()
        
        responce_template = {
         "author": [author[1] for author in author_data],
         "name": book_data[0][1],
         "city": [""],
         "publisher": "",
         "year": book_data[0][2],
         "book": "",
         "theme": [theme[1] for theme in theme_data],
         "knowladge_id": book_data[0][4],
         "age_rating": book_data[0][3],
         "distance": predicted[0]
        }

        responce.append(responce_template)
    
    return jsonify(responce)


"""@app.route('/recommendations/clf/<int:user_id>', methods=["GET"])
@cross_origin()
def get_clf_recommendations_by_user_id(user_id):
    responce = []
    for predicted in range(3): #predicted_list:
        
        test_data = [[ 38487,  39908],
        [  1711, 128165],
        [106958, 317628],
        [ 98101, 379271]]

        responce_template = {
          "predicted": predict_clf(test_data).tolist()
        }

        responce.append(responce_template)
    
    return jsonify(responce)
"""
#app.run()
