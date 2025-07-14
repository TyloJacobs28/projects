class Student:

    def __init__(self, student_id, name, age, major, gpa):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.major = major
        self.gpa = gpa

        def __str__(self):
            return f"ID: {self.student_id} | Name: {self.name} | Age: {self.age} | Major: {self.major} | GPA: {self.gpa} "