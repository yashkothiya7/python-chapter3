# Write a program to handle some built in exceptions like ZeroDivisionError 

try:
    num1 = int(input("Enter numerator: "))
    num2 = int(input("Enter denominator: "))

    result = num1 / num2
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed!")

except ValueError:
    print("Error: Please enter valid integers only!")

except Exception as e:
    print("An unexpected error occurred:", e)

finally:
    print("Program execution completed.")
