# Write a program to handle multiple exceptions 

try:
    filename = input("Enter file name: ")
    f = open(filename, "r")   

    data = f.read()
    number = int(data)       
    result = 100 / number     

    print("Result:", result)
    f.close()

except FileNotFoundError:
    print("Error: The file does not exist!")

except (ValueError, ZeroDivisionError) as e:
    print("Error:", e)
    
except Exception as e:
    print("Unexpected error:", e)

finally:
    print("Program finished.")
