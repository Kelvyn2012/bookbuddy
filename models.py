from db import get_db_connection

def get_all_books():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    conn.close()
    return books

def get_book_by_id(book_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM books WHERE id = %s", (book_id,))
    book = cursor.fetchone()
    conn.close()
    return book

def add_book(data):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO books (title, author, price, published_date) VALUES (%s, %s, %s, %s)",
        (data['title'], data['author'], data['price'], data['published_date'])
    )
    conn.commit()
    conn.close()

def update_book(book_id, data):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE books SET title=%s, author=%s, price=%s, published_date=%s WHERE id=%s",
        (data['title'], data['author'], data['price'], data['published_date'], book_id)
    )
    conn.commit()
    conn.close()

def delete_book(book_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM books WHERE id = %s", (book_id,))
    conn.commit()
    conn.close()
