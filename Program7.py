#Write a program to access the base class constructor and method in a sub class by using  super(). 

class Person:

    # Base class constructor
    def __init__(self, name):
        self.name = name

    # Base class method
    def display(self):
        print("Name:", self.name)


class Student(Person):

    # Sub class constructor
    def __init__(self, name, roll_no):
        super().__init__(name)
        self.roll_no = roll_no

    # Sub class method
    def show(self):
        super().display()
        print("Roll No:", self.roll_no)


# Create object of Student class
student = Student("Om", 101)

student.show()