# Lesson 2 Task 3: display all numbers from n to 1, then remove the first number and repeat while n > 0
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

while number > 0:
	currentNumber = number
	while currentNumber > 0:
		print(currentNumber, end='')
		if currentNumber > 1: print(' ', end='')
		currentNumber = currentNumber - 1
	print('')
	number = number - 1
