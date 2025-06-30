from db import get_db_connection

sample_books = [
    {
        "title": "Atomic Habits",
        "author": "James Clear",
        "price": 14.99,
        "published_date": "2018-10-16"
    },
    {
        "title": "Deep Work",
        "author": "Cal Newport",
        "price": 12.50,
        "published_date": "2016-01-05"
    },
    {
        "title": "The Pragmatic Programmer",
        "author": "Andy Hunt",
        "price": 35.00,
        "published_date": "1999-10-30"
    }
]

def seed_books():
    conn = get_db_connection()
    cursor = conn.cursor()
    for book in sample_books:
        cursor.execute("""
            INSERT INTO books (title, author, price, published_date)
            VALUES (%s, %s, %s, %s)
        """, (book['title'], book['author'], book['price'], book['published_date']))
    conn.commit()
    conn.close()
    print("📚 Sample books added to the database.")

if __name__ == "__main__":
    seed_books()
