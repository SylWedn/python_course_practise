from flask import Flask, render_template, request, redirect, url_for
from models import db, Teacher, Lesson, Student, init_db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

init_db(app)

# Create database tables
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

# Routes and views for teachers
@app.route('/add_teacher', methods=['GET', 'POST'])
def add_teacher():
    if request.method == 'POST':
        name = request.form.get('name')
        teacher = Teacher(name=name)
        db.session.add(teacher)
        db.session.commit()
        return redirect(url_for('add_teacher'))

    teachers = Teacher.query.all()
    return render_template('add_teacher.html', teachers=teachers)

@app.route('/assign_lesson/<int:teacher_id>', methods=['POST'])
def assign_lesson(teacher_id):
    teacher = Teacher.query.get(teacher_id)
    lesson_name = request.form.get('lesson_name')
    lesson = Lesson(name=lesson_name, teacher=teacher)
    db.session.add(lesson)
    db.session.commit()
    return redirect(url_for('add_teacher'))

# Routes and views for students
@app.route('/students')
def students():
    students = Student.query.all()
    return render_template('students.html', students=students)

@app.route('/add_student', methods=['POST'])
def add_student():
    if request.method == 'POST':
        name = request.form.get('name')
        student = Student(name=name)
        db.session.add(student)
        db.session.commit()
        return redirect(url_for('students'))

@app.route('/assign_student_lesson/<int:student_id>', methods=['POST'])
def assign_student_lesson(student_id):
    student = Student.query.get(student_id)
    lesson_id = request.form.get('lesson_id')
    lesson = Lesson.query.get(lesson_id)
    student.lessons.append(lesson)
    db.session.commit()
    return redirect(url_for('students'))

# Routes and views for lessons
@app.route('/lessons')
def lessons():
    lessons = Lesson.query.all()
    return render_template('lessons.html', lessons=lessons)

if __name__ == '__main__':
    app.run(debug=True)