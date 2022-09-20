#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if (number > 0):
    print(f"{number} is greater than 0")
elif (number < 0):
    print(f"{number} is less than 0")
else:
    print(f"{number} is 0")
