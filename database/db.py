# database/db.py
import sqlite3
import os

DB_PATH = os.path.join("data", "leaks.db")
os.makedirs("data", exist_ok=True)

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS leaks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                url TEXT,
                leak_type TEXT,
                content_snippet TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()

def store_leak(url, leak_type, content_snippet):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO leaks (url, leak_type, content_snippet)
            VALUES (?, ?, ?)
        ''', (url, leak_type, content_snippet))
        conn.commit()

init_db()
