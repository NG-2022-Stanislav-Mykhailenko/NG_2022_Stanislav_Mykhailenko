# Lesson 2 Task 4: get number factorial
# Author: Stanislav Mykhailenko
# License: Unlicense

try:
	number = int(input("Enter a natural number: "))
	if number < 1:
		raise ValueError("A natural number is required.")

	factorial = 1

	for i in range(2, number + 1):
		factorial = factorial * i

	print(str(number) + " factorial is " + str(factorial))
except ValueError:
	print("Invalid number entered.")
