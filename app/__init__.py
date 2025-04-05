from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default-secret-key')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///results.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from .routes import main
    app.register_blueprint(main)

    with app.app_context():
        db.create_all()

    # Read both Excel files
    df_sem4 = pd.read_excel('data/results_sem4.xlsx')
    df_sem5 = pd.read_excel('data/results_sem5.xlsx')

    # Display column names for both files
    print("Semester 4 Columns:")
    print(df_sem4.columns.tolist())
    print("\nSemester 5 Columns:")
    print(df_sem5.columns.tolist())

    # Display first few rows of each file
    print("\nSemester 4 Sample Data:")
    print(df_sem4.head())
    print("\nSemester 5 Sample Data:")
    print(df_sem5.head())

    return app 