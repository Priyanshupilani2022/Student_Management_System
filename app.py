from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
import os

app = Flask(__name__)

# MongoDB connection
mongo_uri = os.getenv('MONGO_URI', 'mongodb://localhost:27017/')
client = MongoClient(mongo_uri)
db = client['student_management']
students_collection = db['students']

def calculate_result(student):
    total_marks_obtained = sum(subject['marks_obtained'] for sem in student['semesters'] for subject in sem['subjects'])
    total_max_marks = sum(subject['max_marks'] for sem in student['semesters'] for subject in sem['subjects'])
    student['total_marks_obtained'] = total_marks_obtained
    student['total_max_marks'] = total_max_marks
    student['percentage'] = (total_marks_obtained / total_max_marks) * 100 if total_max_marks > 0 else 0
    if student['percentage'] >= 90:
        student['result'] = 'A'
    elif student['percentage'] >= 80:
        student['result'] = 'B'
    elif student['percentage'] >= 70:
        student['result'] = 'C'
    elif student['percentage'] >= 60:
        student['result'] = 'D'
    else:
        student['result'] = 'F'
    student['status'] = 'Pass' if student['result'] != 'F' else 'Fail'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    try:
        students = list(students_collection.find())
        for student in students:
            student['_id'] = str(student['_id'])
        return render_template('dashboard.html', students=students)
    except Exception as e:
        print(f"Error retrieving students: {e}")
        return "Internal Server Error", 500

@app.route('/view_student/<student_no>')
def view_student(student_no):
    try:
        student = students_collection.find_one({'student_no': student_no})
        if student:
            student['_id'] = str(student['_id'])
            return render_template('view_student.html', student=student)
        return "Student not found", 404
    except Exception as e:
        print(f"Error retrieving student: {e}")
        return "Internal Server Error", 500

@app.route('/add_student', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        try:
            student = {
                'student_no': request.form['student_no'],
                'student_name': request.form['student_name'],
                'class': request.form['class'],
                'semesters': []
            }
            semester_count = int(request.form['semester_count'])
            for i in range(1, semester_count + 1):
                subjects = []
                subject_count = int(request.form[f'subject_count_{i}'])
                for j in range(1, subject_count + 1):
                    subjects.append({
                        'subject_name': request.form[f'subject_name_{i}_{j}'],
                        'marks_obtained': int(request.form[f'marks_obtained_{i}_{j}']),
                        'max_marks': int(request.form[f'max_marks_{i}_{j}'])
                    })
                student['semesters'].append({
                    'semester': i,
                    'subjects': subjects
                })

            # Calculate total marks and percentage
            calculate_result(student)

            students_collection.insert_one(student)
            return redirect(url_for('dashboard'))
        except Exception as e:
            print(f"Error adding student: {e}")
            return "Internal Server Error", 500
    return render_template('add_student.html')

@app.route('/edit_student/<student_no>', methods=['GET', 'POST'])
def edit_student(student_no):
    if request.method == 'POST':
        try:
            updated_student = {
                'student_no': request.form['student_no'],
                'student_name': request.form['student_name'],
                'class': request.form['class'],
                'semesters': []
            }
            semester_count = int(request.form['semester_count'])
            for i in range(1, semester_count + 1):
                subjects = []
                subject_count = int(request.form[f'subject_count_{i}'])
                for j in range(1, subject_count + 1):
                    subjects.append({
                        'subject_name': request.form[f'subject_name_{i}_{j}'],
                        'marks_obtained': int(request.form[f'marks_obtained_{i}_{j}']),
                        'max_marks': int(request.form[f'max_marks_{i}_{j}'])
                    })
                updated_student['semesters'].append({
                    'semester': i,
                    'subjects': subjects
                })

            # Calculate total marks and percentage
            calculate_result(updated_student)

            students_collection.update_one({'student_no': student_no}, {'$set': updated_student})
            return redirect(url_for('dashboard'))
        except Exception as e:
            print(f"Error editing student: {e}")
            return "Internal Server Error", 500
    try:
        student = students_collection.find_one({'student_no': student_no})
        if student:
            student['_id'] = str(student['_id'])
            return render_template('edit_student.html', student=student)
        return "Student not found", 404
    except Exception as e:
        print(f"Error retrieving student for edit: {e}")
        return "Internal Server Error", 500

@app.route('/delete_student/<student_no>', methods=['POST'])
def delete_student(student_no):
    try:
        students_collection.delete_one({'student_no': student_no})
        return redirect(url_for('dashboard'))
    except Exception as e:
        print(f"Error deleting student: {e}")
        return "Internal Server Error", 500

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        try:
            # Your upload handling logic here
            pass
        except Exception as e:
            print(f"Error uploading student data: {e}")
            return "Internal Server Error", 500
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)
