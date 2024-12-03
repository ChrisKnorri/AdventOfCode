import os
from pprint import pprint


with open('/home/knorri/projects/AOC24/day_01/list.txt', 'r') as file:
    lists = file.readlines()
    
    list_left = []
    list_right = []

    for line in lists:
        values = line.split()
        if len(values) >= 2:
            list_left.append(int(values[0]))
            list_right.append(int(values[1]))
            
list_left = sorted(list_left)
list_right = sorted(list_right)

# distances = 0

# for numLeft, numRight in zip(list_left, list_right):
    
#     temp = numLeft - numRight
#     print(f"{numLeft} - {numRight} = {temp}")
#     if(temp <= 0):
#         temp = temp * -1
#         print(f"{temp} is negative!")
    
#     distances += temp

# print(distances)

similarity = 0

for numLeft in list_left:
    cnt = 0
    
    for numRight in list_right:          
        if(numLeft == numRight):
            cnt = cnt + 1
    
    similarity += numLeft * cnt
    
print(similarity)
