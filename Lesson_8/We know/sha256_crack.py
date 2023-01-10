# Lesson 8 Task e1900ba2: SHA-256 crack (?)
# Author: Stanislav Mykhailenko
# License: Unlicense

# Return codes:
# 0 - OK
# 1 - Invalid hash
# 2 - Not cracked

import hashlib, itertools, sys

def hashError():
	print("Invalid SHA-256 hash.")
	sys.exit(1)

crackedHash = input("Enter SHA-256 hash: ")

if len(crackedHash) != 64:
	hashError()

try:
	int(crackedHash, 16)
except ValueError:
	hashError()

for product in itertools.product('abcdefghijklmnopqrstuvwxyz', repeat=4):
	string = ''
	for i in range(len(product)):
		string += product[i]
	if crackedHash == hashlib.sha256(string.encode('utf-8')).hexdigest():
		print("Cracked: " + string)
		sys.exit(0)

print("Not cracked.")
sys.exit(2)
