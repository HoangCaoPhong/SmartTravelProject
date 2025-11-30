"""
Feedback Service using SQLite
"""
import sqlite3
import pandas as pd
from datetime import datetime
import os

# Path to the database file
DB_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "windy_feedback.db")

def init_feedback_db():
    """Initialize the feedback database table."""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            name TEXT,
            email TEXT,
            category TEXT,
            content TEXT,
            status TEXT DEFAULT 'New'
        )
    ''')
    conn.commit()
    conn.close()

def add_feedback(name, email, category, content):
    """Add a new feedback entry."""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    c.execute(
        'INSERT INTO feedback (timestamp, name, email, category, content) VALUES (?, ?, ?, ?, ?)',
        (timestamp, name, email, category, content)
    )
    conn.commit()
    conn.close()

def get_all_feedback():
    """Retrieve all feedback entries."""
    conn = sqlite3.connect(DB_PATH)
    try:
        df = pd.read_sql_query("SELECT * FROM feedback ORDER BY id DESC", conn)
    except Exception:
        df = pd.DataFrame()
    conn.close()
    return df
