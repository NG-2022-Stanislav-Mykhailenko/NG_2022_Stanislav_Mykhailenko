# Lesson 4 Task 1: write system info to a file
# Author: Stanislav Mykhailenko
# License: Unlicense

# Return codes:
# 0 - OK

import platform, psutil, os, serial.tools.list_ports

def getValue(checkedValue):
	if checkedValue:
		return "yes"
	else:
		return "no"

def printList(names, values):
	for number in range(len(names)):
		print(chr(ord("a") + number) + ") " + names[number] + " " + "[" + getValue(values[number]) + "]")
	print("y) Proceed")

def writeData(file, name, code):
	file.write(name + ": " + eval(code) + "\n")

names = ["CPU", "Architecture", "CPU Family", "RAM", "Operating system", "Disk usage", "Serial ports"]
data = [False] * len(names)
code = ["platform.processor()", "str(platform.architecture())", "platform.machine()", "str(psutil.virtual_memory())", "os.name", "str(psutil.disk_usage(\".\"))", "str(serial.tools.list_ports.comports())"]

selection = None
while True:
	printList(names, data)
	selection = input()
	if selection == "y":
		break
	if not len(selection) == 1 or ord(selection) < ord("a") or ord(selection) >= (ord("a") + len(names)):
		print("Invalid selection.")
		continue
	number = ord(selection) - ord("a")
	data[number] = not data[number]

file_out = open("data.txt", "w")

for number in range(len(data)):
	if data[number]:
		writeData(file_out, names[number], code[number])

file_out.close()
