#Write a program to override the super class method in Subclass 

class Animal:
    def sound(self):
        print("Animals make different sounds")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

a = Animal()
d = Dog()
c = Cat()

print("Superclass method call:")
a.sound()

print("\nSubclass (Dog) method call:")
d.sound()

print("\nSubclass (Cat) method call:")
c.sound()
