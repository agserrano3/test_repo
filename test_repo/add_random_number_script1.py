import random

with open('file1.txt', 'r+') as file:
    content = file.read()
    number = random.randint(1, 500)
    file.seek(0)
    file.write(str(number) + content)
