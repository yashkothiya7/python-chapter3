#Write a program to store data into instances using mutator methods and to retrieve data from the instances using accessor methods. 

class Student:
    def __init__(self):
        self.roll_no = None
        self.name = None
        self.age = None

    def set_roll_no(self, roll_no):
        self.roll_no = roll_no

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def get_roll_no(self):
        return self.roll_no

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

s1 = Student()

s1.set_roll_no(101)
s1.set_name("Aakash")
s1.set_age(20)

print("Student Details:")
print("Roll No:", s1.get_roll_no())
print("Name   :", s1.get_name())
print("Age    :", s1.get_age())
