# Lesson 3 Task K3F9#@%^&?: bank card validation
# Author: Stanislav Mykhailenko
# License: Unlicense

# Return codes:
# 0 - OK

def validateLength(number):
	if len(number) < 13 or len(number) > 16 or len(number) == 14:
		return False
	return True

def validateLuhn(number):
	even = False
	evenDigits = ""
	evenSum = 0
	oddSum = 0
	for i in reversed(range(len(number))):
		if even:
			evenDigits += str(int(number[i]) * 2)
		else:
			oddSum += int(number[i])
		even = not even

	for i in range(len(evenDigits)):
		evenSum += int(evenDigits[i])

	if (evenSum + oddSum) % 10 == 0:
		return True
	return False

number = input("Number: ")
if validateLength(number) and validateLuhn(number):
	if len(number) == 13 or len(number) == 16 and number[0] == "4":
		print("VISA")
	elif len(number) == 16 and number[0] == "5" and int(number[1]) >= 1 and int(number[1]) <= 5:
		print("MASTERCARD")
	elif len(number) == 15 and number[0] == "3" and number[1] == "4" or number[1] == "7":
		print("AMEX")
	else:
		print("INVALID")
else:
	print("INVALID")
