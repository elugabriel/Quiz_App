from flask import Flask, render_template, request, session, jsonify, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.expression import func
from datetime import datetime
from config import Config
from models import db, Question, Student, Attempt, AttemptDetail
import json 
import random

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    db.create_all()


# ========== MAIN ROUTES ==========

@app.route("/")
def index():
    """Landing page - choose student or admin"""
    return render_template("index.html")

@app.route("/student/login", methods=["GET", "POST"])
def student_login():
    """Student login page"""
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        cls = request.form.get("class_name", "").strip()
        
        if not name:
            flash("Please enter your name.", "error")
            return render_template("student_login.html")
        
        # Check if student already exists
        student = Student.query.filter_by(name=name, class_name=cls).first()
        if not student:
            student = Student(name=name, class_name=cls)
            db.session.add(student)
            db.session.commit()
        
        session["student_id"] = student.id
        session["student_name"] = student.name
        session["user_type"] = "student"
        
        flash(f"Welcome back, {student.name}!", "success")
        return redirect(url_for("quiz"))
    
    return render_template("student_login.html")

@app.route("/login")
def login():
    """Redirect to student login"""
    return redirect(url_for("student_login"))

@app.route("/register")
def register():
    """Redirect to student login"""
    return redirect(url_for("student_login"))


# ========== STUDENT QUIZ ROUTES ==========

@app.route("/quiz")
def quiz():
    if "student_id" not in session:
        return redirect(url_for("student_login"))

    # Draw a balanced mix: ~75% label, ~25% sort
    n_total = app.config["QUESTIONS_PER_QUIZ"]
    n_sort  = max(3, n_total // 4)
    n_label = n_total - n_sort

    label_qs = (Question.query
                .filter_by(q_type="drag_label")
                .order_by(func.random())
                .limit(n_label).all())

    sort_qs  = (Question.query
                .filter_by(q_type="drag_sort")
                .order_by(func.random())
                .limit(n_sort).all())

    questions = label_qs + sort_qs
    # Shuffle so sort questions don't all appear at the end
    random.shuffle(questions)

    # STORE ALL QUESTION IDs in session
    session["question_ids"] = [q.id for q in questions]
    session["total_questions"] = len(questions)
    session["start_time"] = datetime.utcnow().isoformat()

    return render_template(
        "quiz.html",
        questions=[q.to_dict() for q in questions],
        student_name=session["student_name"],
        total_questions=len(questions)
    )

@app.route("/submit", methods=["POST"])
def submit():
    if "student_id" not in session:
        return jsonify({"error": "Not logged in"}), 401

    data = request.get_json()
    answers = data.get("answers", [])
    
    # Get the total number of questions from session
    total_questions = len(session.get("question_ids", []))
    
    if total_questions == 0:
        total_questions = len(answers)
    
    attempt = Attempt(
        student_id=session["student_id"],
        total=total_questions,
        finished_at=datetime.utcnow()
    )
    db.session.add(attempt)
    db.session.flush()

    results = []
    score = 0
    
    # Create a map of submitted answers by question_id
    answer_map = {item["question_id"]: item for item in answers}
    
    # Loop through ALL questions from the session
    for question_id in session.get("question_ids", []):
        q = Question.query.get(question_id)
        if not q:
            continue
        
        # Check if this question was answered
        if question_id in answer_map:
            item = answer_map[question_id]
            
            # Handle different question types
            if q.q_type == "drag_sort":
                given_array = item.get("answer", [])
                if isinstance(given_array, str):
                    try:
                        given_array = json.loads(given_array)
                    except:
                        given_array = given_array.split(",")
                
                correct_array = q.answer.split(",")
                correct_array = [x.strip().lower() for x in correct_array]
                given_array = [x.strip().lower() for x in given_array]
                correct = given_array == correct_array
                given_str = ",".join(given_array)
                
            else:  # drag_label
                given = item.get("answer", "").strip().lower()
                correct = given == q.answer.strip().lower()
                given_str = given
        else:
            # Question was not answered
            correct = False
            given_str = "(no answer provided)"
        
        if correct:
            score += 1
        
        detail = AttemptDetail(
            attempt_id=attempt.id,
            question_id=q.id,
            given_answer=given_str,
            is_correct=correct
        )
        db.session.add(detail)
        
        results.append({
            "question_id": q.id,
            "q_type": q.q_type,
            "correct": correct,
            "correct_answer": q.answer,
            "image_path": q.image_path,
            "given_answer": given_str,
            "prompt": q.prompt,
        })
    
    # Calculate percentage based on TOTAL questions
    pct = round((score / total_questions) * 100, 1) if total_questions > 0 else 0
    attempt.score = score
    attempt.percentage = pct
    attempt.passed = pct >= app.config["PASS_MARK"]
    db.session.commit()

    return jsonify({
        "score": score,
        "total": total_questions,
        "percentage": pct,
        "passed": attempt.passed,
        "results": results,
    })

@app.route("/leaderboard")
def leaderboard():
    """Return leaderboard page or JSON"""
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        # Return JSON for AJAX requests
        top = (db.session.query(Student.name, Student.class_name,
                                db.func.max(Attempt.percentage).label("best_pct"),
                                db.func.count(Attempt.id).label("attempts"))
               .join(Attempt)
               .group_by(Student.id)
               .order_by(db.desc("best_pct"))
               .limit(10)
               .all())

        rows = [{"name": r.name, "class": r.class_name,
                 "best_pct": r.best_pct, "attempts": r.attempts}
                for r in top]
        return jsonify(rows)
    else:
        # Return HTML page
        return render_template("leaderboard.html")

@app.route("/logout")
def logout():
    """Student logout"""
    session.pop("student_id", None)
    session.pop("student_name", None)
    session.pop("user_type", None)
    flash("Logged out successfully", "success")
    return redirect(url_for("index"))


# ========== ADMIN ROUTES ==========

@app.route("/admin/login", methods=["GET", "POST"])
def admin_login():
    """Admin login page"""
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "").strip()
        
        # Default admin credentials (you should change these in production)
        if username == "admin" and password == "admin123":
            session["admin_id"] = 1
            session["admin_name"] = "Administrator"
            session["user_type"] = "admin"
            flash("Welcome to Admin Dashboard!", "success")
            return redirect(url_for("admin_dashboard"))
        else:
            flash("Invalid admin credentials!", "error")
    
    return render_template("admin_login.html")

@app.route("/admin/dashboard")
def admin_dashboard():
    """Admin dashboard - view all students and their scores"""
    if "admin_id" not in session:
        return redirect(url_for("admin_login"))
    
    # Get all students with their attempt statistics
    students = db.session.query(
        Student.id,
        Student.name,
        Student.class_name,
        db.func.count(Attempt.id).label("total_attempts"),
        db.func.max(Attempt.percentage).label("highest_score"),
        db.func.avg(Attempt.percentage).label("average_score"),
        db.func.sum(Attempt.passed).label("passed_count")
    ).outerjoin(Attempt).group_by(Student.id).order_by(Student.name).all()
    
    # Get recent attempts
    recent_attempts = db.session.query(
        Attempt.id,
        Attempt.score,
        Attempt.percentage,
        Attempt.passed,
        Attempt.finished_at,
        Student.name,
        Student.class_name
    ).join(Student).order_by(Attempt.finished_at.desc()).limit(20).all()
    
    # Overall statistics
    total_students = db.session.query(db.func.count(Student.id)).scalar() or 0
    total_attempts = db.session.query(db.func.count(Attempt.id)).scalar() or 0
    avg_score = db.session.query(db.func.avg(Attempt.percentage)).scalar() or 0
    
    pass_rate_query = db.session.query(
        (db.func.sum(Attempt.passed).cast(db.Float) / db.func.count(Attempt.id) * 100)
    ).scalar()
    pass_rate = pass_rate_query if pass_rate_query else 0
    
    stats = {
        "total_students": total_students,
        "total_attempts": total_attempts,
        "avg_score": avg_score,
        "pass_rate": pass_rate
    }
    
    return render_template(
        "admin_dashboard.html",
        students=students,
        recent_attempts=recent_attempts,
        stats=stats
    )

@app.route("/admin/student/<int:student_id>")
def admin_student_detail(student_id):
    """View detailed attempts for a specific student"""
    if "admin_id" not in session:
        return redirect(url_for("admin_login"))
    
    student = Student.query.get_or_404(student_id)
    attempts = Attempt.query.filter_by(student_id=student_id).order_by(Attempt.finished_at.desc()).all()
    
    return render_template(
        "admin_student_detail.html",
        student=student,
        attempts=attempts
    )

@app.route("/admin/attempt/<int:attempt_id>")
def admin_attempt_detail(attempt_id):
    """View detailed answers for a specific attempt"""
    if "admin_id" not in session:
        return redirect(url_for("admin_login"))
    
    attempt = Attempt.query.get_or_404(attempt_id)
    details = AttemptDetail.query.filter_by(attempt_id=attempt_id).all()
    
    # Get question details
    questions = []
    for detail in details:
        question = Question.query.get(detail.question_id)
        if question:
            questions.append({
                "prompt": question.prompt,
                "q_type": question.q_type,
                "correct_answer": question.answer,
                "given_answer": detail.given_answer,
                "is_correct": detail.is_correct,
                "image_path": question.image_path
            })
    
    return render_template(
        "admin_attempt_detail.html",
        attempt=attempt,
        questions=questions,
        student=attempt.student
    )

@app.route("/admin/export_results")
def admin_export_results():
    """Export all results as CSV"""
    if "admin_id" not in session:
        return redirect(url_for("admin_login"))
    
    import csv
    from io import StringIO
    from flask import Response
    
    # Query all attempts with student info
    results = db.session.query(
        Student.name,
        Student.class_name,
        Attempt.score,
        Attempt.percentage,
        Attempt.passed,
        Attempt.finished_at
    ).join(Attempt).order_by(Attempt.finished_at.desc()).all()
    
    # Create CSV
    output = StringIO()
    writer = csv.writer(output)
    writer.writerow(["Student Name", "Class", "Score", "Percentage", "Passed", "Date"])
    
    for row in results:
        writer.writerow([
            row.name,
            row.class_name if row.class_name else "Not specified",
            f"{row.score}",
            f"{row.percentage}%",
            "Yes" if row.passed else "No",
            row.finished_at.strftime("%Y-%m-%d %H:%M:%S")
        ])
    
    output.seek(0)
    return Response(
        output.getvalue(),
        mimetype="text/csv",
        headers={"Content-Disposition": "attachment;filename=quiz_results.csv"}
    )

@app.route("/admin/logout")
def admin_logout():
    """Admin logout"""
    session.pop("admin_id", None)
    session.pop("admin_name", None)
    session.pop("user_type", None)
    flash("Logged out from admin panel", "success")
    return redirect(url_for("index"))


# ========== HELPER FUNCTIONS ==========

def _check_category(given: dict, expected_str: str) -> bool:
    """
    expected_str format: "input:Keyboard,Mouse|output:Printer,Monitor"
    given format:        {"input": ["Keyboard","Mouse"], "output": ["Printer","Monitor"]}
    """
    try:
        expected = {}
        for part in expected_str.split("|"):
            cat, items = part.split(":")
            expected[cat] = set(i.strip().lower() for i in items.split(","))

        for cat, items in expected.items():
            given_set = set(i.strip().lower() for i in given.get(cat, []))
            if given_set != items:
                return False
        return True
    except Exception:
        return False


if __name__ == "__main__":
    app.run(debug=True)