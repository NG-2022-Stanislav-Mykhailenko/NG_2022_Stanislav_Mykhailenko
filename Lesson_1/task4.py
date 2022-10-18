# Lesson 1 Task 4: quadratic equation calculator
# Author: Stanislav Mykhailenko
# License: Unlicense

# Return codes:
# 0 - OK
# 1 - Invalid numbers entered
# 2 - Not a quadratic equation

import sys, math

try:
	a = float(input("Enter number a: "))
	b = float(input("Enter number b: "))
	c = float(input("Enter number c: "))
except ValueError:
	print("Invalid numbers entered.")
	sys.exit(1)

if a == 0:
	print("Not a quadratic equation.")
	sys.exit(2)

# Discriminant
D = math.pow(b, 2) - 4 * a * c

if D < 0:
	print("No real roots exist.")
elif D >= 0:
	print("x₁ = " + str((-b + math.sqrt(D)) / (2 * a)))
	if D > 0:
		print("x₂ = " + str((-b - math.sqrt(D)) / (2 * a)))
