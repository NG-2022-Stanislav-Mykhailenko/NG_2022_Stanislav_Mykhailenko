# Lesson 2 Task 4: get number factorial
# Author: Stanislav Mykhailenko
# License: Unlicense

# Return codes:
# 0 - OK
# 1 - Invalid number entered

import sys

def numberError():
	print("Invalid number entered.")
	sys.exit(1)

try: number = int(input("Enter a natural number: "))
except ValueError: numberError()

if number < 1: numberError()

factorial = 1

for i in range(2, number + 1):
	factorial = factorial * i
else:
	print(str(number) + " factorial is " + str(factorial))
