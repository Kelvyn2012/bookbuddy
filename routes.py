from flask import Blueprint, jsonify, request
from models import get_all_books, get_book_by_id, add_book, update_book, delete_book

book_routes = Blueprint('book_routes', __name__)

@book_routes.route('/books', methods=['GET'])
def list_books():
    return jsonify(get_all_books())

@book_routes.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = get_book_by_id(book_id)
    if book:
        return jsonify(book)
    return jsonify({'error': 'Book not found'}), 404

@book_routes.route('/books', methods=['POST'])
def create_book():
    data = request.json
    add_book(data)
    return jsonify({'message': 'Book added successfully'}), 201

@book_routes.route('/books/<int:book_id>', methods=['PUT'])
def modify_book(book_id):
    data = request.json
    update_book(book_id, data)
    return jsonify({'message': 'Book updated successfully'})

@book_routes.route('/books/<int:book_id>', methods=['DELETE'])
def remove_book(book_id):
    delete_book(book_id)
    return jsonify({'message': 'Book deleted successfully'})
