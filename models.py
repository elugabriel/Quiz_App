from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json

db = SQLAlchemy()


class Question(db.Model):
    __tablename__ = "questions"
    id           = db.Column(db.Integer, primary_key=True)
    topic        = db.Column(db.String(100))
    q_type       = db.Column(db.String(50))
    image_path   = db.Column(db.String(200))
    prompt       = db.Column(db.String(300))
    answer       = db.Column(db.String(100))
    options      = db.Column(db.Text)  # Changed from JSON to Text
    difficulty   = db.Column(db.String(20))
    created_at   = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        # Parse options from JSON string back to list
        try:
            options_list = json.loads(self.options)
        except:
            # If already a list or comma separated
            if isinstance(self.options, list):
                options_list = self.options
            else:
                options_list = [opt.strip() for opt in self.options.split(',')]
        
        return {
            "id": self.id,
            "topic": self.topic,
            "q_type": self.q_type,
            "image_path": self.image_path,
            "prompt": self.prompt,
            "options": options_list,  # This will be a proper list
            "answer": self.answer,
            "difficulty": self.difficulty
        }


class Student(db.Model):
    __tablename__ = "students"
    id         = db.Column(db.Integer, primary_key=True)
    name       = db.Column(db.String(100), nullable=False)
    class_name = db.Column(db.String(50))
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