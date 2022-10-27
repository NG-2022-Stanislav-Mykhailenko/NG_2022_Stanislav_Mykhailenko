# Lesson 2 Task 5: sort a comma-separated array of numbers, output the smallest and the biggest elements, and the sum of the rest elements
# Author: Stanislav Mykhailenko
# License: Unlicense

# Return codes:
# 0 - OK

def is_float(number):
	try:
		float(number)
	except ValueError:
		return False
	return True

list = [element for element in list(dict.fromkeys(input("Enter a comma-separated list: ").split(','))) if is_float(element)] # remove all duplicates and non-number values

if len(list) == 0:
	print("The list is empty")
else:
	list.sort(key = float)
	print(list)

	print ("The " + ("only" if len(list) == 1 else "smallest") + " element is: " + str(list[0]))
	list.remove(list[0])

	if len(list) > 0:
		print ("The biggest element is: " + str(list[-1]))
		list.remove(list[-1])

		if len(list) > 0:
			sum = 0

			for elem in list:
				sum = sum + float(elem)
			print(sum)
