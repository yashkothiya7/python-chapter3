#Write a program to check the object type to know whether the method exists in the object or not. 
class Student:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"Student Name: {self.name}")

class Teacher:
    def __init__(self, subject):
        self.subject = subject

    def teach(self):
        print(f"Teaching : {self.subject}")

s1 = Student("Aakash")
t1 = Teacher("Mathematics")

print("Checking methods in Student object:")
print("Has display? :", hasattr(s1, "display"))
print("Has teach?   :", hasattr(s1, "teach"))

print("\nChecking methods in Teacher object:")
print("Has display? :", hasattr(t1, "display"))
print("Has teach?   :", hasattr(t1, "teach"))
print()

if hasattr(s1, "display"):
    s1.display()
else:
    print("Does not exist!")

if hasattr(t1, "teach"):
    t1.teach()
else:
    print("Does not exist!")