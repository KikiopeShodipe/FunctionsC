# Define the functions
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b
# Ask user for choice
print("Choose operation: +, -, *, /")
op = input("Enter operator: ")
# Ask for numbers
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
# Perform operation
if op == "+":
    print("Result:", add(a, b))
elif op == "-":
    print("Result:", subtract(a, b))
elif op == "*":
    print("Result:", multiply(a, b))
elif op == "/":
    if b != 0:
        print("Result:",divide(a, b))
    else:
        print("cannot divide by 0")
else:
    print("invalid input")