# main.py

from students import Student
import manager
import db

def print_menu():
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student by ID")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

def run():
    db.create_table()

    while True:
        print_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            student_id = input("ID: ")
            name = input("Name: ")
            age = int(input("Age: "))
            major = input("Major: ")
            gpa = float(input("GPA: "))
            student = Student(student_id, name, age, major, gpa)
            manager.add_student(student)
            print("✅ Student added.")

        elif choice == "2":
            students = manager.get_all_students()
            for s in students:
                print(s)

        elif choice == "3":
            sid = input("Enter student ID: ")
            student = manager.find_student_by_id(sid)
            print(student if student else "❌ Student not found.")

        elif choice == "4":
            sid = input("Enter student ID to update: ")
            student = manager.find_student_by_id(sid)
            if student:
                name = input(f"New name [{student.name}]: ") or student.name
                age = input(f"New age [{student.age}]: ") or student.age
                major = input(f"New major [{student.major}]: ") or student.major
                gpa = input(f"New GPA [{student.gpa}]: ") or student.gpa
                updated = Student(sid, name, int(age), major, float(gpa))
                manager.update_student(updated)
                print("✅ Student updated.")
            else:
                print("❌ Student not found.")

        elif choice == "5":
            sid = input("Enter student ID to delete: ")
            manager.delete_student(sid)
            print("✅ Student deleted.")

        elif choice == "6":
            print("Exiting... 👋")
            break

        else:
            print("⚠️ Invalid option, try again.")

if __name__ == "__main__":
    run()
