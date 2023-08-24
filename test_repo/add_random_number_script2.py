import random

with open('file_dos.txt', 'r+') as file:
    contents = file.readlines()
    chosen_line = random.choice([0, 1])
    number = random.randint(1, 100)
    contents[chosen_line] = str(number) + contents[chosen_line]
    file.seek(0)
    file.writelines(contents)

