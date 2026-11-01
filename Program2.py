#Write a program to demonstrate the use of instance and class/static variables 

class Student:

    # Class variable
    college = "ABC College"

    def __init__(self, name, age):
        # Instance variables
        self.name = name
        self.age = age


# Create objects
s1 = Student("Om", 20)
s2 = Student("Rahul", 21)

# Display instance variables
print("Student 1 Name:", s1.name)
print("Student 1 Age:", s1.age)

print("Student 2 Name:", s2.name)
print("Student 2 Age:", s2.age)

# Display class variable
print("College:", Student.college)