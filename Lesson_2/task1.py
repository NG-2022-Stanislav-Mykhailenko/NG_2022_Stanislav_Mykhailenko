# Lesson 2 Task 1: calculate a number of each letter occurences in a string, output it sorted by letters and by numbers
# Author: Stanislav Mykhailenko
# License: Unlicense

# Return codes:
# 0 - OK

occurences = {}
string = input("Enter a string: ")

for element in string:
	if element in occurences: occurences[element] = occurences[element] + 1
	else: occurences[element] = 1

print("Occurrences sorted by letter: " + str(dict(sorted(occurences.items()))))
print("Occurrences sorted by number: " + str(dict(sorted(occurences.items(), key=lambda item: item[1], reverse=True))))
