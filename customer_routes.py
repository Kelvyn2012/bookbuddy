from flask import Blueprint, jsonify, request
from db import get_db_connection

customer_routes = Blueprint('customer_routes', __name__)  # <- THIS line is important

@customer_routes.route('/customers', methods=['GET'])
def get_customers():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM customers")
    customers = cursor.fetchall()
    conn.close()
    return jsonify(customers)

@customer_routes.route('/customers', methods=['POST'])
def create_customer():
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO customers (name, email, address) VALUES (%s, %s, %s)",
        (data['name'], data['email'], data['address'])
    )
    conn.commit()
    conn.close()
    return jsonify({'message': 'Customer added successfully'}), 201
