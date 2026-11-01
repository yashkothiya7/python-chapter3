#Create a Student class to with the methods set_id, get_id, set_name, get_name, set_marks and get_marks where the method name 
# starting with set are used to assign the values and method name starting with get are returning the values. Save the program 
# by student.py. Create another program to use the Student class which is already available in student.py. 

from Student_p6 import Student   

s1 = Student()

s1.set_id(101)
s1.set_name("Aakash")
s1.set_marks(92)

print("Student Details:")
print("ID    :", s1.get_id())
print("Name  :", s1.get_name())
print("Marks :", s1.get_marks())
