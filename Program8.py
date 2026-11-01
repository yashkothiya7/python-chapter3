#Write a program to implement single inheritance in which two sub classes are derived from a single base class. 
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age : {self.age}")

class Student(Person):
    def __init__(self, name, age, roll_no, marks):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.marks = marks

    def display(self):
        super().display()
        print(f"Roll No: {self.roll_no}")
        print(f"Marks  : {self.marks}")

class Teacher(Person):
    def __init__(self, name, age, subject, salary):
        super().__init__(name, age)
        self.subject = subject
        self.salary = salary

    def display(self):
        super().display()
        print(f"Subject: {self.subject}")
        print(f"Salary : {self.salary}")

s1 = Student("Aakash", 20, 101, 92)
t1 = Teacher("Himanshu", 35, "Mathematics", 50000)

print("Student Details:")
s1.display()

print("\nTeacher Details:")
t1.display()
