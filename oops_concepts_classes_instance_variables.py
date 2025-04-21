class Student:

    num_of_students = 0 #class attribute

    def __init__(self, name):
        self.name = name
        print("New student created:", name)
        Student.num_of_students += 1
        self.grades = []

    def add_grades(self, course, grade):
        self.grades.append((course, grade))
        print(f"Grade {grade} added for te course {course}")

    @classmethod
    def class_count(cls):
        return cls.num_of_students

