import pandas as pd
from app.database import db
from app.models import Student, Result  # You'll need to create these models

def load_excel_data():
    """Load data from Excel files and initialize the database."""
    try:
        # Load semester 4 data
        df_sem4 = pd.read_excel('data/cleaned_sem4.xlsx')
        
        # Load semester 5 data
        df_sem5 = pd.read_excel('data/cleaned_sem5.xlsx')
        
        # Process and insert data into the database
        for _, row in df_sem4.iterrows():
            student = Student(
                roll_no=row['Roll_No'],
                name=row['Name'],
                gender=row['Gender']
            )
            db.session.add(student)
            
            result = Result(
                student=student,
                semester=4,
                sgpa=row['SGPA'],
                cgpa=row['CGPA'],
                result=row['Result']
            )
            db.session.add(result)
        
        # Similar process for semester 5
        for _, row in df_sem5.iterrows():
            student = Student.query.filter_by(roll_no=row['Roll_No']).first()
            if not student:
                student = Student(
                    roll_no=row['Roll_No'],
                    name=row['Name'],
                    gender=row['Gender']
                )
                db.session.add(student)
            
            result = Result(
                student=student,
                semester=5,
                sgpa=row['SGPA'],
                cgpa=row['CGPA'],
                result=row['Result']
            )
            db.session.add(result)
        
        # Commit all changes
        db.session.commit()
        print("Data initialization completed successfully!")
        
    except Exception as e:
        print(f"Error initializing data: {str(e)}")
        db.session.rollback() 