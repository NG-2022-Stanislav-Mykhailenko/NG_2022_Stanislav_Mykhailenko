# Lesson 2 Task 3: display all numbers from n to 1, then remove the first number and repeat while n > 0
# Author: Stanislav Mykhailenko
# License: Unlicense

try:
	number = int(input("Enter a natural number: "))
	if number < 1:
		raise ValueError("A natural number is required.")

	for biggestNumber in range(number, 0, -1):
		for currentNumber in range(biggestNumber, 0, -1):
			print(currentNumber, end='')
			if currentNumber > 1: print(' ', end='')
		print('')

except ValueError:
	print("Invalid number entered.")
