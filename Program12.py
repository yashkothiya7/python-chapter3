# Write a program to overload the addition operator (+) to make it act on the class objects. 
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def __add__(self, other):       
        return self.marks + other.marks

    def display(self):
        print(f"Name: {self.name}, Marks: {self.marks}")

s1 = Student("Aakash", 85)
s2 = Student("Rutvi", 90)   

s1.display()
s2.display()

# sum of s1 object with calling __add__(s2)so, 85 + 90
total_marks = s1 + s2  
print("\nTotal Marks of both students:", total_marks)

