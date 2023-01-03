# Lesson 2 Task 4: get number factorial
# Author: Stanislav Mykhailenko
# License: Unlicense

error = False

try: number = int(input("Enter a natural number: "))
except ValueError: error = True

if not error and number < 1: error = True

if not error:
	factorial = 1

	for i in range(2, number + 1):
		factorial = factorial * i
	else:
		print(str(number) + " factorial is " + str(factorial))
else:
	print("Invalid number entered.")