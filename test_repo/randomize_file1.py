import random

with open('test_repo/file1.txt', 'r+') as file:
    content = file.read()
    number = random.randint(1, 500)  # Generating random number between 1 and 500
    file.seek(0)
    file.write(str(number) + content)
