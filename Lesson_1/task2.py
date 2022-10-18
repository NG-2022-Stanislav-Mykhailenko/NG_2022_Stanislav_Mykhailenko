# Lesson 1 Task 2: calculator
# Author: Stanislav Mykhailenko
# License: Unlicense

# Return codes:
# 0 - OK
# 1 - Invalid numbers entered
# 2 - Division by zero
# 3 - Invalid first operation entered
# 4 - Square root of a negative number calculation

import sys, math

try:
	numberA = float(input("Enter number A: "))
	numberB = float(input("Enter number B: "))
except ValueError:
	print("Invalid numbers entered.")
	sys.exit(1)

operation = input("Enter operation (+, − or -, × or *, ÷ or /): ")

# The other part of the task is not clearly defined. It asks to implement square root of a number, or its square, but it can only be done with one number. Assuming it is the result of the first operation and saving it…
result: float

if operation == "+":
	result = numberA + numberB
elif operation == "-" or operation == "−": # ASCII hyphen-minus or Unicode minus
	result = numberA - numberB
elif operation == "*" or operation == "×": # ASCII asterisk or Unicode multiplication sign
	result = numberA * numberB
elif operation == "/" or operation == "÷": # ASCII slash or Unicode division sign
	if numberB == 0:
		print("Division by zero.")
		sys.exit(2)
	else:
		result = numberA / numberB
else:
	print("Invalid operation.")
	sys.exit(3)

print("Result: " + str(result))

# …and asking to do sqrt or square with it.
secondOperation = input("Do anything else with the result (√ or sqrt, ² or square, any other input will be ignored)? ")

if secondOperation == "√" or secondOperation == "sqrt": # Unicode radical symbol
	if result < 0:
		print("Can't get a square root of a negative number.")
		sys.exit(4)
	else:
		print(math.sqrt(result))
elif secondOperation == "²" or secondOperation == "square": # Unicode superscript 2
	print(math.pow(result, 2))
