from flask import Flask, jsonify, request
from pymongo import MongoClient
from flask import render_template
'''
import os

app = Flask(__name__)

if 'MONGO_URI' in os.environ and 'APP_ENV' in os.environ:
    mongo_uri = os.environ.get('MONGO_URI')
    app_env = os.environ.get('APP_ENV')
else:
    mongo_uri = "mongodb://briksam:vH8l1cjIoOH2CM6w80qXJVj9z6qrFFC2pgAxjXSDGmIKlq1gdjLCjNOdTIW6NMM7wP7Maqh2bZHGACDb8zDLww==@briksam.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@briksam@"
    app_env = "python"
'''

app = Flask(__name__)

client = MongoClient('mongodb://briksam:vH8l1cjIoOH2CM6w80qXJVj9z6qrFFC2pgAxjXSDGmIKlq1gdjLCjNOdTIW6NMM7wP7Maqh2bZHGACDb8zDLww==@briksam.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@briksam@')


db = client["Bookstore"]

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/')
def Bookstore():
    return 'MY BOOKSTORE!'

@app.route('/api/allbooks', methods=['GET'])
def get_books():
    books = list(db.bookstore.find({}, {"_id": 0}))
    return jsonify({'books': books})

@app.route('/api/books/<isbn>', methods=['GET'])
def get_book_by_isbn(isbn):
    book = db.bookstore.find_one({'isbn': isbn}, {"_id": 0})
    if book:
        return jsonify({'book': book})
    else:
        return jsonify({'error': 'Book not found'}), 404



@app.route('/api/books', methods=['POST'])
def add_book():
    new_book = request.json
    result = db.bookstore.insert_one(new_book)
    return jsonify({'message': 'Book added successfully', 'id': str(result.inserted_id)})


@app.route('/api/books/<isbn>', methods=['PUT'])
def update_book(isbn):
    updated_data = request.json
    result = db.bookstore.update_one({'isbn': isbn}, {'$set': updated_data})
    if result.modified_count > 0:
        return jsonify({'message': 'Book updated successfully'})
    else:
        return jsonify({'error': 'Book not found or no changes made'}), 404


@app.route('/api/books/<isbn>', methods=['DELETE'])
def delete_book(isbn):
    result = db.bookstore.delete_one({'isbn': isbn})
    if result.deleted_count > 0:
        return jsonify({'message': 'Book deleted successfully'})
    else:
        return jsonify({'error': 'Book not found'}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5005)
