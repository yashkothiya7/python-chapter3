# create a Student class with a constructor having more than one parameter. Also create a method named display() to view the student details. 

class Student:
    def __init__(self, roll_no, name, age, course):
        self.roll_no = roll_no
        self.name = name
        self.age = age
        self.course = course

    def display(self):
        print("Student Details:")
        print(f"Roll No : {self.roll_no}")
        print(f"Name    : {self.name}")
        print(f"Age     : {self.age}")
        print(f"Course  : {self.course}")


student_obj1 = Student(101, "Aakash", 20, "Computer Science")
student_obj2 = Student(102, "Rutvi", 19, "Information Technology")

student_obj1.display()
print()
student_obj2.display()
        