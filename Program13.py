# Write a program to show method overloading to find sum of two or three numbers

class Calculator:
    def sum(self, *args):
        return sum(args)

calc = Calculator()

print("Sum of 2 numbers:", calc.sum(5, 15))

print("Sum of 3 numbers:", calc.sum(5, 15, 25))
