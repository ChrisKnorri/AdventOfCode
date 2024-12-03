import os
import re
from pprint import pprint

memory = ""

with open('/home/knorri/projects/AOC24/day_03/input.txt', 'r') as file:
    for line in file:
        memory += line.strip()  # `strip()` removes newline characters


# Regex mul_pattern for "mult(" + 1-3 digit int + "," + 1-3 digit int + ")"
mul_pattern = r"(mul\(\d{1,3},\d{1,3}\))"
dont_pattern = r"don\'t\(\)(.*?)do\(\)"

dos_only = re.sub(dont_pattern, "", memory)

values = re.findall(mul_pattern, dos_only)

# Define a mul() function
def mul(a, b):
    return a * b

products = [eval(command) for command in values]
    
pprint(products)

print(sum(products))
# distances = 0

# for numLeft, numRight in zip(list_left, list_right):
    
#     temp = numLeft - numRight
#     print(f"{numLeft} - {numRight} = {temp}")
#     if(temp <= 0):
#         temp = temp * -1
#         print(f"{temp} is negative!")
    
#     distances += temp

# print(distances)