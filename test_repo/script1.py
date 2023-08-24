import random

with open('file1.txt', 'r') as file:
    contents = file.read()
number = random.randint(1, 10000)  # generate number between 1 and 10000
print(f"{number}{contents}", end='')  # add number in the beginning
# print(f"{contents}{number}", end='')  # uncomment this to add number in the end
