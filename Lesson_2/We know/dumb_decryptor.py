# Lesson 2 Task %*f#ncA0#>?: ROT13 encryption
# Author: Stanislav Mykhailenko
# License: Unlicense

# Return codes:
# 0 - OK

rot13 = str.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz', 
   'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm')

print(input("Enter message: ").translate(rot13))
