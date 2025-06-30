from flask import Flask
from routes import book_routes
from db import init_db

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to BookBuddy API. Try /books"


# Register blueprints
app.register_blueprint(book_routes)

# Initialize DB (optional for first-time setup)
init_db()

if __name__ == '__main__':
    app.run(debug=True)
