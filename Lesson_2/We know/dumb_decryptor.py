# Lesson 2 Task %*f#ncA0#>?: ROT13 encryption
# Author: Stanislav Mykhailenko
# License: Unlicense

# Return codes:
# 0 - OK

def isUppercase(chr):
	if chr >= "A" and chr <= "Z":
		return True
	else:
		return False

def isLowercase(chr):
	if chr >= "a" and chr <= "z":
		return True
	else:
		return False

def isLetter(chr):
	if isUppercase(chr) or isLowercase(chr):
		return True
	else:
		return False

string = input("Enter message: ")
newstring = ''

for i in range(len(string)):
	if not isLetter(string[i]):
		continue
	uppercase = isUppercase(string[i])
	newOrd = ord(string[i]) + 13
	if isLetter(chr(newOrd)) and uppercase == isUppercase(chr(newOrd)):
		newstring += chr(newOrd)
	else:
		newstring += chr(newOrd - 26)

print(newstring)
