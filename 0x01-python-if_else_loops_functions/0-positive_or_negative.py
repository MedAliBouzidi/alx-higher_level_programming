#!/usr/bin/python3
import random
number = random.randint(-10, 10)
message = f"{number} "
if number > 0:
    message += "is positive"
elif number < 0:
    message += "is negative"
else:
    message += "is zero"
print(message)
