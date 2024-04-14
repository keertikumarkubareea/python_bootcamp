"""Introduction to the random number generator in python

"""

import random

i = random.randint(0, 100)  # Both inclusive

#  Printing 100 random numbers from 0 to 100 inclusive
count = 1
while count <= 100:
    print(i)
    i = random.randint(0, 100)  # Both inclusive
    print(f"Count: {count}")
    count += 1
    print("--------------------------------")
