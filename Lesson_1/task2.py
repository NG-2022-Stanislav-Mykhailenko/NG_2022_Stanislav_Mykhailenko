# Lesson 1 Task 2: calculator
# Author: Stanislav Mykhailenko
# License: Unlicense

# Return codes:
# 0 - OK
# 1 - Invalid numbers entered
# 2 - Division by zero
# 3 - Attempting to use a root with non-natural degree
# 4 - Attempting to extract a root of a negative number with an even degree
# 5 - Invalid operation entered

try:
	numberA = float(input("Enter number A: "))
	numberB = float(input("Enter number B: "))
except ValueError:
	print("Invalid numbers entered.")
	exit(1)

print(
'''
Valid operations:
Addition: +
Subtraction: - or −
Multiplication: * or ×
Division: / or ÷
Root: root or √ (extracted from the first number, with the second number being its degree)
Square: square or ² (of both numbers)''', end="\n\n"
)

operation = input("Enter operation: ")

if operation == "+":
	print(numberA + numberB)
elif operation == "-" or operation == "−": # ASCII hyphen-minus or Unicode minus
	print(numberA - numberB)
elif operation == "*" or operation == "×": # ASCII asterisk or Unicode multiplication sign
	print(numberA * numberB)
elif operation == "/" or operation == "÷": # ASCII slash or Unicode division sign
	if numberB == 0:
		print("Division by zero.")
		exit(2)
	else:
		print(numberA / numberB)
elif operation == "root" or operation == "√": # Unicode radical symbol
	if numberB < 1 or not numberB.is_integer():
		print("Can't extract a root with non-natural degree.")
		exit(3)
	elif (numberB % 2) == 0 and numberA < 0:
		print("Can't extract a root of a negative number with an even degree.")
		exit(4)
	else:
		if numberA < 0:
			print(-abs(numberA ** (1 / numberB)))
		else:
			print(numberA ** (1 / numberB))
elif operation == "square" or operation == "²": # Unicode superscript 2
	print("Number A square: " + str(numberA ** 2) + "\nNumber B square: " + str(numberB ** 2))
else:
	print("Invalid operation.")
	exit(5)
