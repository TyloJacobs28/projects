# db.py

import sqlite3

def get_connection():
    return sqlite3.connect("students.db")

def create_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            student_id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER,
            major TEXT,
            gpa REAL
        );
    """)
    conn.commit()
    conn.close()
