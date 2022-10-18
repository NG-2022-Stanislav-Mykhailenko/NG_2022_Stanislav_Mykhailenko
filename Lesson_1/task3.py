# Lesson 1 Task 3: calculate how much time passed since Unix epoch
# Author: Stanislav Mykhailenko
# License: Unlicense

# Return codes:
# 0 - OK
# 1 - Invalid Unix timestamp entered

import sys

try:
	timestamp = int(input("Enter Unix timestamp: "))
except ValueError:
	print("Invalid Unix timestamp entered.")
	sys.exit(1)

# duration in seconds
day = 86400 # 24 * hour
hour = 3600 # 60 * minute
minute = 60

days = int(timestamp / day)
hours = int(int(timestamp % day) / hour)
minutes = int(int(int(timestamp % day) % hour) / minute)
seconds = int(int(timestamp % day) % hour) % minute

print(str(days) + ":" + str(hours) + ":" + str(minutes) + ":" + str(seconds))
