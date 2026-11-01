# #create a static method that counts the number of instances created for a class. 
# class Student:
#     count = 0
#     instances = []
#     def __init__(self,name):
#         self.name = name
#         Student.count += 1
#         Student.instances.append(self)
    
#     def count_instance():
#         return Student.count
    
#     def show_name(self):
#         print("Student Name:", self.name)

# s1 = Student("Aakash")
# s2 = Student("Rutvi")
# s3 = Student("monil")
# print("Total instances of class is : ",Student.count_instance())

# print("\nCreated Student Instances:")
# for stu in Student.instances:
#     stu.show_name()


class Student:

    count = 0
    instances = []

    def __init__(self, name):
        self.name = name
        Student.count += 1
        Student.instances.append(self)

    @staticmethod
    def count_instances():
        return Student.count
    
    def show_name(self):
        print("Student Name:", self.name)


# Create objects
s1 = Student("Om")
s2 = Student("Rahul")
s3 = Student("Amit")

# Display number of instances
print("Number of instances created:", Student.count_instances())


print("\nCreated Student Instances:")
for stu in Student.instances:
    stu.show_name()
