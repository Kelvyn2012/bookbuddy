from flask import Flask
from routes import book_routes
from customer_routes import customer_routes
from order_routes import order_routes

app = Flask(__name__)
app.register_blueprint(book_routes)
app.register_blueprint(customer_routes)
app.register_blueprint(order_routes)

@app.route('/')
def home():
    return "Welcome to BookBuddy API. Try /books, /customers, or /orders"

if __name__ == '__main__':
    app.run(debug=True)
