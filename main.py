
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import Base, engine, SessionLocal
import models
from auth import hash_password, verify_password, create_token
import webbrowser


app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

# Root route (so / doesn't show Not Found)
@app.get("/")
def home():
    return {"message": "server working"}

# Database connection
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ---------------- AUTH ----------------

@app.post("/api/v1/auth/register", tags=["Auth"])


def register(email: str, password: str, db: Session = Depends(get_db)):
    # Email validation
    if "@" not in email:
        raise HTTPException(status_code=400, detail="Invalid email format")

    # Password validation
    if len(password) < 6:
        raise HTTPException(status_code=400, detail="Password must be at least 6 characters")

    existing_user = db.query(models.User).filter(models.User.email == email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    user = models.User(email=email, password=hash_password(password))
    db.add(user)
    db.commit()
    token = create_token({"email": email})
    return {"token": token}

@app.post("/api/v1/auth/login", tags=["Auth"])


def login(email: str, password: str, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == email).first()

    if not user or not verify_password(password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_token({"email": email})
    return {"token": token}

# ---------------- STUDENTS ----------------

@app.post("/api/v1/students", tags=["Students"])


def create_student(name: str, email: str, course: str, year: int,semester:int,enrollment_date:str, gpa: float,status:str, phone: str,attendance_percentage:float,address:str,emergency_contact:str, db: Session = Depends(get_db)):
    # Email check
    if "@" not in email:
        raise HTTPException(status_code=400, detail="Invalid student email")

    # Year check
    if year < 1 or year > 4:
        raise HTTPException(status_code=400, detail="Year must be between 1 and 4")

    # GPA check
    if gpa < 0 or gpa > 10:
        raise HTTPException(status_code=400, detail="GPA must be between 0 and 10")

    # Attendance check
    if attendance_percentage < 0 or attendance_percentage > 100:
        raise HTTPException(status_code=400, detail="Attendance must be between 0 and 100")
    student = models.Student(name=name, email=email, course=course, year=year,semester = semester,enrollment_date = enrollment_date, gpa=gpa,status=status, phone=phone,attendance_percentage = attendance_percentage,address=address,emergency_contact=emergency_contact)
    db.add(student)
    db.commit()
    return {"message": "Student added"}

@app.get("/api/v1/students", tags=["Students"])


def get_students(
    course: str = None,
    year: int = None,
    db: Session = Depends(get_db)
):
    query = db.query(models.Student)

    if course:
        query = query.filter(models.Student.course == course)

    if year:
        query = query.filter(models.Student.year == year)

    return query.all()
webbrowser.open("http://127.0.0.1:8000/docs")

