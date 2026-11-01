#Write a program to use class method to handle the Common features of all the instance of Student class. 

class Student:
    school_name = "som-lalit public School"

    def __init__(self, roll_no, name, age):
        self.roll_no = roll_no
        self.name = name
        self.age = age

    def display(self):
        print("Roll No:", self.roll_no)
        print("Name   :", self.name)
        print("Age    :", self.age)
        print("School :", Student.school_name)

    @classmethod
    def change_school(cls, new_name):
        cls.school_name = new_name
        print(f"School name updated to: {cls.school_name}")

s1 = Student(101, "Aakash", 20)
s2 = Student(102, "Rutvi", 19)

print("Before changing school name:\n")
s1.display()
print()
s2.display()

print("\nUpdating school name using class method...")
Student.change_school("Muni International School")

print("\nAfter changing school name:\n")
s1.display()
print()
s2.display()
