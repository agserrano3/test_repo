import random

with open('file2.txt', 'r') as file:
    contents = file.read().splitlines()

random_line = random.choice([0, 1])  # choose random line to add number
number = random.randint(1, 10000)  # generate number between 1 and 10000

contents[random_line] = f"{number}{contents[random_line]}"  
#uncomment below to add number in the end
#contents[random_line] = f"{contents[random_line]}{number}" 

for line in contents:
    print(line)
    
