# order_routes.py
from flask import Blueprint, jsonify, request
from db import get_db_connection
from datetime import date

order_routes = Blueprint('order_routes', __name__)

@order_routes.route('/orders', methods=['GET'])
def get_orders():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT o.id AS order_id, o.order_date, c.name AS customer_name
        FROM orders o
        JOIN customers c ON o.customer_id = c.id
    """)
    orders = cursor.fetchall()
    conn.close()
    return jsonify(orders)

@order_routes.route('/orders', methods=['POST'])
def create_order():
    data = request.json
    customer_id = data['customer_id']
    order_date = data.get('order_date', date.today().isoformat())

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO orders (customer_id, order_date) VALUES (%s, %s)",
        (customer_id, order_date)
    )
    order_id = cursor.lastrowid

    for item in data['items']:  
        cursor.execute(
            "INSERT INTO order_details (order_id, book_id, quantity) VALUES (%s, %s, %s)",
            (order_id, item['book_id'], item['quantity'])
        )

    conn.commit()
    conn.close()
    return jsonify({'message': 'Order created successfully', 'order_id': order_id}), 201
