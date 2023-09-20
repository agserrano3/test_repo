import random
import argparse
import datetime
import pytz
  
parser = argparse.ArgumentParser(description='Random calculator. Use --time option to display current time in Pacific timezone.')
parser.add_argument('--time', action='store_true', help='Print the current time in Pacific timezone.')
args = parser.parse_args()
  
if args.time:
    pacific = pytz.timezone('US/Pacific')
    print(f"Current Pacific Time: {datetime.datetime.now(pacific)}")

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
