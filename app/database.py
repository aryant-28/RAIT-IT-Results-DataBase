import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_db(app):
    # Get database URL from environment variable or use SQLite as fallback
    database_url = os.environ.get('DATABASE_URL', 'sqlite:///instance/results.db')
    
    # Configure SQLAlchemy
    app.config['SQLALCHEMY_DATABASE_URI'] = database_url
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Initialize the database
    db.init_app(app)
    
    # Create all tables
    with app.app_context():
        db.create_all() 