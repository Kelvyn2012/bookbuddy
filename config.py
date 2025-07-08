# Database configuration
import os
from dotenv import load_dotenv

load_dotenv()  # Loads variables from .env into environment

MYSQL_CONFIG = {
    "host": os.getenv("localhost"),
    "user": os.getenv("root"),
    "password": os.getenv("Jenifer2012%"),
    "database": os.getenv("bookbuddyDB"),
}
