# add_module_topic.py
from app import app, db
from models import Attempt
import sqlite3

with app.app_context():
    # Check if column exists
    import sqlite3
    conn = sqlite3.connect('instance/quiz.db')  # Change to your database path if different
    cursor = conn.cursor()
    
    # Check if module_topic column exists
    cursor.execute("PRAGMA table_info(attempts)")
    columns = [column[1] for column in cursor.fetchall()]
    
    if 'module_topic' not in columns:
        print("Adding module_topic column to attempts table...")
        cursor.execute("ALTER TABLE attempts ADD COLUMN module_topic VARCHAR(200) DEFAULT 'General Quiz'")
        conn.commit()
        print("✅ Column added successfully!")
    else:
        print("✅ module_topic column already exists!")
    
    conn.close()