from flask import Flask
from app.database import init_db, db
import os
from dotenv import load_dotenv
import pandas as pd
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default-secret-key')
    
    # Use in-memory SQLite database if DATABASE_URL is not provided
    # This is safer for cloud environments with ephemeral filesystems
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///:memory:')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize the database
    init_db(app)

    # Register blueprints
    from app.routes import main
    app.register_blueprint(main)

    with app.app_context():
        try:
            db.create_all()
            logger.info("Database tables created successfully")
        except Exception as e:
            logger.error(f"Error creating database tables: {str(e)}")

    # Load Excel data
    try:
        # Check if files exist before trying to load
        if os.path.exists('data/results_sem4.xlsx') and os.path.exists('data/results_sem5.xlsx'):
            # Read both Excel files
            df_sem4 = pd.read_excel('data/results_sem4.xlsx')
            df_sem5 = pd.read_excel('data/results_sem5.xlsx')

            # Display column names for both files
            logger.info("Semester 4 Columns:")
            logger.info(df_sem4.columns.tolist())
            logger.info("Semester 5 Columns:")
            logger.info(df_sem5.columns.tolist())

            # Display first few rows of each file
            logger.info("Semester 4 Sample Data:")
            logger.info(df_sem4.head())
            logger.info("Semester 5 Sample Data:")
            logger.info(df_sem5.head())
        else:
            logger.warning("Excel data files not found in the expected location.")
    except Exception as e:
        logger.error(f"Error loading Excel data: {str(e)}")

    return app 