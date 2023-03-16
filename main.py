# Simple Calculator Program in Python with a user-friendly interface

def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


def exponent(x, y):
    return x ** y


def modulo(x, y):
    return x % y


def floor_divide(x, y):
    return x // y

print("JITI'S PYTHON LEARNING ##")
print("Welcome to the Simple Calculator!")
print("Please select the type of calculation you want to perform:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exponentiation")
print("6. Modulo")
print("7. Floor Division")

# Take input from the user
choice = input("Enter your choice(1/2/3/4/5/6/7): ")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if choice == '1':
    print("The sum of", num1, "and", num2, "is", add(num1, num2))

elif choice == '2':
    print("The difference between", num1, "and", num2, "is", subtract(num1, num2))

elif choice == '3':
    print("The product of", num1, "and", num2, "is", multiply(num1, num2))

elif choice == '4':
    print("The quotient of", num1, "and", num2, "is", divide(num1, num2))

elif choice == '5':
    print(num1, "raised to the power of", num2, "is", exponent(num1, num2))

elif choice == '6':
    print("The remainder when", num1, "is divided by", num2, "is", modulo(num1, num2))

elif choice == '7':
    print("The floor division of", num1, "and", num2, "is", floor_divide(num1, num2))

else:
    print("Invalid input")
