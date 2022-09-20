#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
negative = 0
if (number < 0):
    negative = number
    number = number * -1
lastDigit = number % 10
if (negative < 0):
    lastDigit = lastDigit * -1
    number = number * -1
if (lastDigit % 10 > 5):
    print(f"Last digit of {number} is {lastDigit}"
          " and is greater than 5")
elif (lastDigit % 10 < 6 and lastDigit != 0):
    print(f"Last digit of {number} is {lastDigit} "
          "and is less than 6 and not 0")
else:
    print(f"Last digit of {number} is {lastDigit} and is 0")
