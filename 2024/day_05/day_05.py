import os
import re
from pprint import pprint
import math

def findIndex(list, value):
    for index, x in enumerate(list):
        if x == value:
            return index
    return -1

def carryOutOrderingRule(list, rules):
    for rule in rules:
        x_position = findIndex(list, rule[0])
        y_position = findIndex(list, rule[1])
        
        if x_position > y_position:
            list[x_position], list[y_position] = list[y_position], list[x_position]         
    
    return list

def orderList(list, rules):
    for line in list:
        length = len(line)
        for num in line:
            current_index = findIndex(num)
            for i in range(length):
                
            
        

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Define the file path relative to the script's directory
input_path = os.path.join(current_dir, 'input.txt')
rule_path = os.path.join(current_dir, 'rules.txt')

# Open the file and read the input
with open(input_path, 'r') as file:
    # Read lines, strip whitespace, and split by commas, then convert to int
    input = [[int(num) for num in line.strip().split(',')] for line in file]

# Open the file and read the rules
with open(rule_path, 'r') as file:
    # Read lines, strip whitespace, and split by commas, then convert to int
    rules = [[int(num) for num in line.strip().split('|')] for line in file]


pprint(rules)
# Flatten the rules list
rule_numbers = [num for sublist in rules for num in sublist]

# Remove duplicate occurrences of numbers in rule_numbers
rule_numbers = list(set(rule_numbers))

print(rule_numbers)


rule_numbers = carryOutOrderingRule(rule_numbers, rules)

print(rule_numbers)

rule_numbers = carryOutOrderingRule(rule_numbers, rules)

print(rule_numbers)

def sumUpMiddleNumbers(list):
    sum = 0

    for line in list:
        length = len(line)
        middle_number = math.floor(length / 2)
        sum += line[middle_number]
        
    return sum

print(sumUpMiddleNumbers())