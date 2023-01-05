# Lesson 3 Task 3: calculate a number of each letter occurrences in a string without using loops
# Author: Stanislav Mykhailenko
# License: Unlicense

# Return codes:
# 0 - OK

def getOccurrences(string, occurrences, currentElement):
	if string[currentElement] in occurrences: occurrences[string[currentElement]] = occurrences[string[currentElement]] + 1
	else: occurrences[string[currentElement]] = 1
	if currentElement + 1 < len(string):
		getOccurrences(string, occurrences, currentElement + 1)

	

occurrences = {}
string = input("Enter a string: ")

getOccurrences(string, occurrences, 0)

print("Occurrences sorted by letter: " + str(dict(sorted(occurrences.items()))))
print("Occurrences sorted by number: " + str(dict(sorted(occurrences.items(), key=lambda item: item[1], reverse=True))))
