# Student_Management_System

A comprehensive web application to manage student information, built with Flask and MongoDB. This project includes functionalities for adding, viewing, and managing student details, including their performance across multiple semesters.

# Features
  Add New Student: Input student details including name, number, class, and marks for multiple subjects across different semesters.
  View Student Details: Display detailed student information, including subject-wise marks and overall performance.
  Dashboard: Overview of all students with options to view, edit, and delete student records.
  Data Upload: Option to enter data via a form or upload a document for automated data extraction.
  Custom Logic: Calculate total and overall marks, percentage, and determine pass/fail status based on predefined criteria.

# Technologies Used
  Frontend: HTML, CSS, JavaScript, Bootstrap
  Backend: Python, Flask
  Database: MongoDB
  Environment: Virtual Environment (venv)

#  Setup Instructions
Clone the Repository:
  git clone https://github.com/yourusername/student_management.git
  cd student_management

# Set Up Virtual Environment:
  python -m venv env
  source env\Scripts\activate

# Configure Environment Variables:
Create a .env file in the root directory with the following content:
  DB_NAME=student_management
  COLLECTION_NAME=students
  MONGO_URI=mongodb://localhost:27017/

# Run the Application:
  flak run

# Project Structure 
student_management/
├── env/
├── static/
│   ├── css/
│   │   └── bootstrap.min.css
│   ├── js/
│   │   └── bootstrap.bundle.min.js
├── templates/
│   ├── add_student.html
│   ├── dashboard.html
│   ├── index.html
│   ├── view_student.html
├── .env
├── .gitignore
├── app.py
└── README.md

# Screenshots


![Screenshot (46)](https://github.com/user-attachments/assets/0e626c00-1127-4b3c-a0d7-b1862348e1aa)

![image](https://github.com/user-attachments/assets/5f33980b-5b65-4268-a9cc-6ae4af0522af)

![image](https://github.com/user-attachments/assets/da3c4d6f-ac68-4e71-b719-030e8c424f83)

![image](https://github.com/user-attachments/assets/7f120fef-e574-4b85-8a4f-5a7e4824e0e6)

![image](https://github.com/user-attachments/assets/170372db-8c0e-46a7-abf1-0216594f1964)

![image](https://github.com/user-attachments/assets/472c23fd-2f65-4e0c-9b5a-7bcbddc3f647)







