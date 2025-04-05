"""
WSGI entry point. This file provides another way to run the Flask application.
"""
from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run() 