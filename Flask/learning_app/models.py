from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def init_db(app):
    db.init_app(app)

# Teacher model
class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    lessons = db.relationship('Lesson', backref='teacher', lazy=True)

# Lesson model
class Lesson(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    teacher_id = db.Column(db.Integer, db.ForeignKey('teacher.id'), nullable=False)

# Student model
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    lessons = db.relationship('Lesson', secondary='student_lessons', backref='students')

# Many-to-many relationship table
student_lessons = db.Table('student_lessons',
    db.Column('student_id', db.Integer, db.ForeignKey('student.id'), primary_key=True),
    db.Column('lesson_id', db.Integer, db.ForeignKey('lesson.id'), primary_key=True)
)
