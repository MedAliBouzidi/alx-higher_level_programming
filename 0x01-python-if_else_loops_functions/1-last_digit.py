#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ld = abs(number) % 10
if number < 0:
    ld = -ld
message = f"Last digit of {number} is {ld} "
if ld % 10 > 5:
    message += "and is greater than 5"
elif ld % 10 == 0:
    message += "and is 0"
else:
    message += "and is less than 6 and not 0"
print(message)
