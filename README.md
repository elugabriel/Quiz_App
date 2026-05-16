# CompuQuiz — Interactive Computer Science Quiz System

A drag-and-drop CBT-style quiz platform for secondary school students (SS1–SS3).
Built with **Python Flask + Vanilla JavaScript + SQLite**.

---

## Quick Start

```bash
# 1. Create & activate virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Generate placeholder images (replace with real photos later)
python generate_placeholders.py

# 4. Seed the database with questions
python seed.py

# 5. Run the development server
flask run
# Open http://localhost:5000
```

---

## Project Structure

```
quiz_app/
├── app.py                  # Flask routes & scoring engine
├── config.py               # App configuration
├── models.py               # SQLAlchemy database models
├── seed.py                 # Populate DB with questions
├── generate_placeholders.py# Create placeholder component images
├── requirements.txt
├── static/
│   ├── images/             # Hardware component images (.png/.jpg)
│   ├── css/style.css       # Full stylesheet
│   └── js/drag_quiz.js     # Drag-and-drop engine + results renderer
└── templates/
    ├── base.html           # Layout shell
    ├── login.html          # Student name/class entry
    └── quiz.html           # Interactive quiz page
```

---

## Question Types

| `q_type`        | Interaction                              | Example                        |
|-----------------|------------------------------------------|--------------------------------|
| `drag_label`    | Drag a chip onto an image's drop zone    | Identify CPU, RAM, GPU…        |
| `drag_sort`     | Reorder list items by dragging           | Boot sequence steps            |
| `drag_category` | Sort items into Input / Output buckets   | Classify devices by type       |

---

## Adding Real Questions

Edit **`seed.py`** and add entries to the `questions` list. For `drag_label`:

```python
{
    "topic":      "Computer Hardware",
    "q_type":     "drag_label",
    "image_path": "images/your_image.png",   # place in static/images/
    "prompt":     "Identify this component",
    "answer":     "CPU",
    "options":    ["CPU", "RAM", "GPU", "HDD"],
    "difficulty": "easy"      # easy | medium | hard
}
```

Re-run `python seed.py` after adding questions.

---

## Configuration (`config.py`)

| Setting               | Default | Description                  |
|-----------------------|---------|------------------------------|
| `QUESTIONS_PER_QUIZ`  | 10      | Questions shown per session  |
| `PASS_MARK`           | 50      | Minimum % to pass            |
| `SECRET_KEY`          | (dev)   | Change for production!       |

---

## Production Deployment (Render)

1. Push project to GitHub.
2. Create a **Web Service** on [render.com](https://render.com).
3. **Build command:** `pip install -r requirements.txt`
4. **Start command:** `gunicorn app:app`
5. Add environment variables:
   - `SECRET_KEY` — a long random string
   - `DATABASE_URL` — your PostgreSQL connection string (Render PostgreSQL add-on)

The SQLAlchemy code works with both SQLite and PostgreSQL — no code changes needed.
