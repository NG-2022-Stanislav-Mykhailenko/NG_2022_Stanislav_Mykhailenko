# Lesson 4 Task 1: write system info to a file
# Author: Stanislav Mykhailenko
# License: Unlicense

# Return codes:
# 0 - OK

import platform, psutil

data = [False,False,False,False]
selection = None
while True:
	selection = input("a) CPU [" + str(data[0]) + "]\nb) RAM [" + str(data[1]) + "]\nc) Architecture [" + str(data[2]) + "]\nd) CPU Family [" + str(data[3]) + "]\ny) Proceed\n")
	if selection == "y":
		break
	if not len(selection) == 1 or ord(selection) < ord("a") or ord(selection) > ord("d"):
		print("Invalid selection.")
		continue
	number = ord(selection) - ord("a")
	data[number] = not data[number]

anythingTrue = False
if data[0] or data[1] or data[2] or data[3]:
	anythingTrue = True

if anythingTrue:
	file_out = open("data.txt", "w")

	if data[0]:
		file_out.write("CPU: " + platform.processor() + "\n")
	if data[1]:
		file_out.write("RAM: " + str(psutil.virtual_memory()) + "\n")
	if data[2]:
		file_out.write("Architecture: " + str(platform.architecture()) + "\n")
	if data[3]:
		file_out.write("CPU family: " + platform.machine() + "\n")

	file_out.close()
