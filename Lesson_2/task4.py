# Lesson 2 Task 4: get number factorial
# Author: Stanislav Mykhailenko
# License: Unlicense

# Return codes:
# 0 - OK
# 1 - Invalid number entered

import math, sys

def numberError():
	print("Invalid number entered.")
	sys.exit(1)

try: number = int(input("Enter a natural number: "))
except ValueError: numberError()

if number < 1: numberError()

print(str(number) + " factorial is " + str(math.factorial(number)))
