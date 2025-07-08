from db import get_db_connection
from datetime import date

def seed_data():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Sample books
    books = [
        ("Atomic Habits", "James Clear", 14.99, "2018-10-16"),
        ("Deep Work", "Cal Newport", 12.50, "2016-01-05"),
        ("The Pragmatic Programmer", "Andy Hunt", 35.00, "1999-10-30"),
        ("Clean Code", "Robert C. Martin", 30.00, "2008-08-11"),
        ("Think and Grow Rich", "Napoleon Hill", 9.99, "1937-03-01"),
    ]
    cursor.executemany("INSERT INTO books (title, author, price, published_date) VALUES (%s, %s, %s, %s)", books)

    # Sample customers
    customers = [
        ("Alice Johnson", "alice@example.com", "123 Maple St, Lagos"),
        ("Bob Smith", "bob@example.com", "456 Banana Rd, Abuja"),
    ]
    cursor.executemany("INSERT INTO customers (name, email, address) VALUES (%s, %s, %s)", customers)

    # Sample orders
    orders = [
        (1, date(2024, 6, 1)),  # Alice's order
        (2, date(2024, 6, 2)),  # Bob's order
    ]
    cursor.executemany("INSERT INTO orders (customer_id, order_date) VALUES (%s, %s)", orders)

    # Sample order details
    order_details = [
        (1, 1, 2),  # Alice ordered 2 copies of book ID 1
        (1, 3, 1),  # Alice also ordered 1 copy of book ID 3
        (2, 2, 1),  # Bob ordered 1 copy of book ID 2
    ]
    cursor.executemany("INSERT INTO order_details (order_id, book_id, quantity) VALUES (%s, %s, %s)", order_details)

    conn.commit()
    conn.close()
    print("📚 Sample books, customers, and orders added successfully.")

if __name__ == "__main__":
    seed_data()
