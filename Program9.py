# Write a program to implement multiple inheritance using two base classes. 

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print(f"Name: {self.name}")
        print(f"Age : {self.age}")

class Course:
    def __init__(self, course_name, duration):
        self.course_name = course_name
        self.duration = duration

    def display_course(self):
        print(f"Course  : {self.course_name}")
        print(f"Duration: {self.duration} months")

class Student(Person, Course):
    def __init__(self, name, age, course_name, duration, roll_no):
        Person.__init__(self, name, age)
        Course.__init__(self, course_name, duration)
        self.roll_no = roll_no

    def display_student(self):
        self.display_person()
        self.display_course()
        print(f"Roll No : {self.roll_no}")

s1 = Student("Aakash", 20, "Computer Science", 36, 101)

print("Student Details:")
s1.display_student()
