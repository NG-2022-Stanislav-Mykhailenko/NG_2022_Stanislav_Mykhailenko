# Lesson 3 Task 1: calculator with functions
# Author: Stanislav Mykhailenko
# License: Unlicense

# Return codes:
# 0 - OK
# 1 - Invalid numbers entered
# 2 - Division by zero
# 3 - Attempting to use a root with non-natural degree
# 4 - Attempting to extract a root of a negative number with an even degree
# 5 - Invalid operation entered

import sys

def add (a, b): return a + b
def substract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b):
	if b == 0:
		print("Division by zero.")
		sys.exit(2)
	else:
		return a / b
def square(number): return number**2

def isNatural(number): return False if number < 1 or not number.is_integer() else True
def isEven(number): return True if (number % 2) == 0 else False
def isNegative(number): return True if number < 0 else False

def root(number, degree):
	if not isNatural(degree):
		print("Can't extract a root with non-natural degree.")
		sys.exit(3)
	elif isEven(degree) and isNegative(number):
		print("Can't extract a root of a negative number with an even degree.")
		sys.exit(4)
	else:
		if number < 0:
			return -abs(number ** (1 / degree))
		else:
			return number ** (1 / degree)

try:
	numberA = float(input("Enter number A: "))
	numberB = float(input("Enter number B: "))
except ValueError:
	print("Invalid numbers entered.")
	sys.exit(1)

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
	print(add(numberA, numberB))
elif operation == "-" or operation == "−": # ASCII hyphen-minus or Unicode minus
	print(substract(numberA, numberB))
elif operation == "*" or operation == "×": # ASCII asterisk or Unicode multiplication sign
	print(multiply(numberA, numberB))
elif operation == "/" or operation == "÷": # ASCII slash or Unicode division sign
	print(divide(numberA, numberB))
elif operation == "root" or operation == "√": # Unicode radical symbol
	print(root(numberA, numberB))
elif operation == "square" or operation == "²": # Unicode superscript 2
	print("Number A square: " + str(square(numberA)) + "\nNumber B square: " + str(square(numberB)))
else:
	print("Invalid operation.")
	sys.exit(5)
