# Write a program to understand the order of execution of methods in several base classes according to method resolution order (MRO) 

class A:
    def show(self):
        print("Method of Class A")

class B(A):
    def show(self):
        print("Method of Class B")
        super().show()

class C(A):
    def show(self):
        print("Method of Class C")
        super().show()

class D(B, C):
    def show(self):
        print("Method of Class D")
        super().show()

obj = D()
obj.show()

print("\nMethod Resolution Order (MRO):")
# for cls in D.__mro__:
#     print(cls)
print(D.__mro__)