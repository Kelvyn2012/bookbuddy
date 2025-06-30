import mysql.connector
from config import MYSQL_CONFIG

def get_db_connection():
    return mysql.connector.connect(**MYSQL_CONFIG)

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(255) NOT NULL,
        author VARCHAR(255),
        price DOUBLE,
        published_date DATE
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS customers (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255),
        address TEXT
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        id INT AUTO_INCREMENT PRIMARY KEY,
        customer_id INT,
        order_date DATE,
        FOREIGN KEY (customer_id) REFERENCES customers(id)
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS order_details (
        id INT AUTO_INCREMENT PRIMARY KEY,
        order_id INT,
        book_id INT,
        quantity INT,
        FOREIGN KEY (order_id) REFERENCES orders(id),
        FOREIGN KEY (book_id) REFERENCES books(id)
    );
    """)

    conn.commit()
    conn.close()

