# Lesson 3 Task 2: provide a menu with various functions for a string
# Author: Stanislav Mykhailenko
# License: Unlicense

# Return codes:
# 0 - OK

def get_vowels(string):
    vowels = "AaEeIiOoUu"
    result = [each for each in string if each in vowels]
    return result

def get_consonants(string):
    consonants = "BbCcDdFfGgHhJjKkLlMmNnPpQqRrSsTtVvWwXxYyZz"
    result = [each for each in string if each in consonants]
    return result


string = input("Enter a string: ")

operation = input("Enter operation number\n1. Sort the string\n2. Count the elements number\n3. Output vowels\n4. Output consonants\n5. Output the words in reverse order\n6. Output the original string\n\nAny other input will exit the program.\n")

if operation == str(1):
	print("Sorted string: " + str(sorted(string)))
elif operation == str(2):
	print("String length: " + str(len(string)))
elif operation == str(3):
	print("Vowels: " + str(get_vowels(string)))
elif operation == str(4):
	print("Consonants: " + str(get_consonants(string)))
elif operation == str(5):
	reversed = reversed(string.split (" "))
	print("String words in reverse order: ")
	print([each for each in reversed])
elif operation == str(6):
	print("Original string: " + string)
