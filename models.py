from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class Question(db.Model):
    __tablename__ = "questions"
    id           = db.Column(db.Integer, primary_key=True)
    topic        = db.Column(db.String(100))   # e.g. "Computer Hardware"
    q_type       = db.Column(db.String(50))    # "drag_label" | "drag_sort" | "drag_match" | "drag_category"
    image_path   = db.Column(db.String(200))   # "images/cpu.png"
    prompt       = db.Column(db.String(300))   # "Drag the correct label to this component"
    answer       = db.Column(db.String(100))   # Correct answer string
    options      = db.Column(db.JSON)          # ["CPU","RAM","GPU","HDD"]
    difficulty   = db.Column(db.String(20))    # "easy"|"medium"|"hard"
    created_at   = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "topic": self.topic,
            "q_type": self.q_type,
            "image_path": self.image_path,
            "prompt": self.prompt,
            "options": self.options,
            # NOTE: Never include "answer" here!
        }


class Student(db.Model):
    __tablename__ = "students"
    id         = db.Column(db.Integer, primary_key=True)
    name       = db.Column(db.String(100), nullable=False)
    class_name = db.Column(db.String(50))     # e.g. "SS2A"
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    attempts   = db.relationship("Attempt", backref="student")


class Attempt(db.Model):
    __tablename__ = "attempts"
    id          = db.Column(db.Integer, primary_key=True)
    student_id  = db.Column(db.Integer, db.ForeignKey("students.id"))
    score       = db.Column(db.Integer, default=0)
    total       = db.Column(db.Integer)
    percentage  = db.Column(db.Float)
    passed      = db.Column(db.Boolean, default=False)
    started_at  = db.Column(db.DateTime, default=datetime.utcnow)
    finished_at = db.Column(db.DateTime)
    details     = db.relationship("AttemptDetail", backref="attempt")


class AttemptDetail(db.Model):
    __tablename__ = "attempt_details"
    id           = db.Column(db.Integer, primary_key=True)
    attempt_id   = db.Column(db.Integer, db.ForeignKey("attempts.id"))
    question_id  = db.Column(db.Integer, db.ForeignKey("questions.id"))
    given_answer = db.Column(db.String(100))
    is_correct   = db.Column(db.Boolean)
