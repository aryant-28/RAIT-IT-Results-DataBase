from app.database import db

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    roll_no = db.Column(db.String(20), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    gender = db.Column(db.String(10))
    results = db.relationship('Result', backref='student', lazy=True)

class Result(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    semester = db.Column(db.Integer, nullable=False)
    sgpa = db.Column(db.Float)
    cgpa = db.Column(db.Float)
    result = db.Column(db.String(10)) 