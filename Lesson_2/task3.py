# Lesson 2 Task 3: display all numbers from n to 1, then remove the first number and repeat while n > 0
# Author: Stanislav Mykhailenko
# License: Unlicense

error = False

try: number = int(input("Enter a natural number: "))
except ValueError: error = True

if not error and number < 1: error = True

if not error:
	while number > 0:
		currentNumber = number
		while currentNumber > 0:
			print(currentNumber, end='')
			if currentNumber > 1: print(' ', end='')
			currentNumber = currentNumber - 1
		print('')
		number = number - 1
else:
		print("Invalid number entered.")
