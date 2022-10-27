# Lesson 2 Task 2: remove duplicates from a list
# Author: Stanislav Mykhailenko
# License: Unlicense

# Return codes:
# 0 - OK

print(list(dict.fromkeys(input("Enter a comma-separated list: ").split(','))))
