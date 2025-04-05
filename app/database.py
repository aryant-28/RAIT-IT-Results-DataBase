import os
from flask_sqlalchemy import SQLAlchemy
import re

db = SQLAlchemy()

def init_db(app):
    # Get database URL from environment variable or use SQLite as fallback
    database_url = os.environ.get('DATABASE_URL', 'sqlite:///instance/results.db')
    
    # Fix for Render Postgres URL (if it starts with postgres://)
    if database_url.startswith("postgres://"):
        database_url = database_url.replace("postgres://", "postgresql://", 1)
    
    # Configure SQLAlchemy
    app.config['SQLALCHEMY_DATABASE_URI'] = database_url
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Initialize the database
    db.init_app(app)
    
    # Create all tables
    with app.app_context():
        db.create_all() 