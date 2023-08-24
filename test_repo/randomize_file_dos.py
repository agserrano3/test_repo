import random

with open('test_repo/file_dos.txt', 'r+') as file:
    contents = file.readlines()
    chosen_line = random.choice([0, 1]) # Choosing a random line to add the number
    number = random.randint(1, 100) # Generating a random number between 1 and 100
    contents[chosen_line] = str(number) + contents[chosen_line]
    file.seek(0)
    file.writelines(contents)
