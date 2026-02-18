from sqlalchemy import Column, Integer, String, Float
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True)
    password = Column(String)

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    course = Column(String)
    year = Column(Integer)
    semester = Column(Integer)
    enrollment_date = Column(String)
    gpa = Column(Float)
    status = Column(String)
    phone = Column(String)
    attendance_percentage = Column(Float)
    address = Column(String)
    emergency_contact = Column(String)
    
