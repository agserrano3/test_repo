🌈
import random

print("Welcome to the Random Calculator!")

# Ask user for two numbers
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

# Define the algebraic operations
operations = {
    "Addition": lambda a, b: a + b,
    "Subtraction": lambda a, b: a - b,
    "Multiplication": lambda a, b: a * b,
    "Division": lambda a, b: a / b
}

# Select a random operation
operation_name, operation = random.choice(list(operations.items()))

# Apply the operation to the numbers
result = operation(num1, num2)

print(f"The operation was {operation_name}, and the result is {result}")