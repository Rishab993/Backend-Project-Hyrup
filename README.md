## SECTION 1 — Project Setup Instructions

1. Clone the repo
2. Install dependencies:
   pip install fastapi uvicorn sqlalchemy passlib[bcrypt] python-jose
3. Run server:
   python -m uvicorn main:app --reload
4. Open:
   http://127.0.0.1:8000/docs

## SECTION 2 — Environment Variables
secret key = secret123

## SECTION 3 — Database Setup

Database is auto-created when server runs.
File: students.db
No manual setup required.


## SECTION 4 — API Endpoint Documentation

- POST /api/v1/auth/register
- POST /api/v1/auth/login
- POST /api/v1/students
- GET /api/v1/students



## SECTION 5 — Student Model Explanation

- name – student full name  
- email – student email  
- course – enrolled course  
- year – academic year  
- gpa – performance score  
- phone – contact number  
- attendance_percentage – attendance tracking  
- address – residential address  
- emergency_contact – guardian phone  



# SECTION 6 — Design Decisions

1.Used JWT for authentication

2.Used SQLite for simplicity

3.Added filtering on students

4.Added input validation

5.Used API versioning (/api/v1)

