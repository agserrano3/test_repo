import random
import time

# Before you generate a random number, get the current time and store it in a variable.
start_time = time.time()

# Generate a random number
random_integer = random.randint(1, 10)
random_float = random.random()

# Immediately after generating the number, get the current time again and store it in another variable.
end_time = time.time()

# The difference in these two times is the time taken to generate the random number. You can print this.
print('Time taken to generate a random integer and float in Python: ', end_time - start_time)
