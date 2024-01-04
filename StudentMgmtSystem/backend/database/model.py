from StudentMgmtSystem.extensions import (
    db,
)
from sqlalchemy.sql import func


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    age = db.Column(db.Integer)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    bio = db.Column(db.Text)

    def __repr__(self):
        return f"<Student {self.firstname}>"


def add_values():
    sammy = Student(
        firstname="Sammy",
        lastname="Shark",
        email="sammyshark@example.com",
        age=20,
        bio="Marine biology student",
    )

    carl = Student(
        firstname="Carl",
        lastname="White",
        email="carlwhite@example.com",
        age=22,
        bio="Marine geology student",
    )

    student_john = Student(
        firstname="john",
        lastname="doe",
        email="jd@example.com",
        age=23,
        bio="Biology student",
    )

    db.session.add_all([sammy, carl, student_john])
    db.session.commit()
