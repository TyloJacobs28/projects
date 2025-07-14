from db import get_connection
from students import Student

def add_student(student):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students VALUES (?,?,?,?,?)",
                   (student.student_id, student.name, student.age, student.major, student.gpa))

    conn.commit()
    conn.close()

def get_all_students():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students")
        rows = cursor.fetchall()
        conn.close()
        return [Student(*row) for row in rows]

def find_student_by_id(student_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE student_id = ?", (student_id,))
    row = cursor.fetchone()
    conn.close()
    return Student(*row) if row else None

def update_student(student):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
                    UPDATE students
                    SET name = ?, age = ?, major = ?, gpa = ?
                    WHERE student_id = ?""",
                   (student.name, student.age, student.major, student.gpa, student.student_id))
    conn.commit()
    conn.close()

    def delete_student(student_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM students WHERE student_id = ?", (student_id,))
        conn.commit()
        conn.close()


