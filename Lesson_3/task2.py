# Lesson 3 Task 2: provide a menu with various functions for a string
# Author: Stanislav Mykhailenko
# License: Unlicense

# Return codes:
# 0 - OK

def get_vowels(string):
    vowels = "aeiou"
    result = [each for each in string if each.lower() in vowels]
    return result

def get_consonants(string):
    consonants = "bcdfghjklmnpqrstvwxyz"
    result = [each for each in string if each.lower() in consonants]
    return result


string = input("Enter a string: ")

operation = input("Enter operation number\n1. Sort the string\n2. Count the elements number\n3. Output vowels\n4. Output consonants\n5. Output the words in reverse order\n6. Output the original string\n\nAny other input will exit the program.\n")

match operation:
	case '1':
		print("Sorted string: " + str(sorted(string)))
	case '2':
		print("String length: " + str(len(string)))
	case '3':
		print("Vowels: " + str(get_vowels(string)))
	case '4':
		print("Consonants: " + str(get_consonants(string)))
	case '5':
		reversed = reversed(string.split (" "))
		print("String words in reverse order: ")
		print([each for each in reversed])
	case '6':
		print("Original string: " + string)
