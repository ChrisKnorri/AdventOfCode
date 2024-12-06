import os
import re
from pprint import pprint
import math

def getIndex(list, value):
    for index, x in enumerate(list):
        if x == value:
            return index
    return -1

def findMiddleNumber(line):
    length = len(line)
    middle_index = math.floor(length / 2)
    num = line[middle_index]
    
    return num

def getDependencies(num, rules): 
    dependencies = []
    
    for rule in rules:                              # iterate through the rules  
        if num == rule[0]:                          # check for each rule pair if the number is the first number in the pair
            dependencies.append(rule)               # if it is, add the rule to the dependencies list
            
    return dependencies
    
def calculateCorrectMiddleNumbers(input, rules):
    sum = 0
    index = 0  # Index to track current line in the input
    
    while index < len(input):  # Iterate through the input list
        line = input[index]  # Current line
        order_correct = True
        middle_number = findMiddleNumber(line)  # Find the middle number in the line
        
        for num in line:  # Iterate through the numbers in the line
            dependencies = getDependencies(num, rules)  # Get the dependencies of the number
            num_index = getIndex(line, num)  # Get the index of the number in the line
            
            for dependency in dependencies:  # Iterate through the dependencies
                dependant = dependency[1]  # Get the second number in the rule
                dependant_index = getIndex(line, dependant)  # Get the index of the second number in the line
                
                if dependant_index == -1:  # If the second number in the rule is not in the line
                    continue
                elif num_index > dependant_index:  # If the first number is after the second number in the line
                    order_correct = False
                    break
            
            if not order_correct:
                break
        
        if order_correct:
            sum += middle_number
            input.pop(index)  # Remove the current line from the input
        else:
            index += 1  # Move to the next line if not removing the current one

    return sum

from collections import defaultdict, deque
from collections import defaultdict, deque

def orderLines(input, rules):
    def build_graph_for_line(line, rules):
        """
        Build a subgraph and calculate in-degrees based on the rules for the given line.
        """
        graph = defaultdict(list)
        in_degree = defaultdict(int)
        line_set = set(line)

        # Only include rules relevant to the current line
        for a, b in rules:
            if a in line_set and b in line_set:
                graph[a].append(b)
                in_degree[b] += 1
                if a not in in_degree:
                    in_degree[a] = 0  # Ensure all nodes are in the in-degree map

        return graph, in_degree

    def topological_sort_with_cycles(graph, in_degree):
        """
        Perform topological sort for a single line, handling cycles by ignoring conflicting edges.
        """
        queue = deque([node for node in in_degree if in_degree[node] == 0])
        sorted_line = []
        visited = set()

        while queue:
            node = queue.popleft()
            sorted_line.append(node)
            visited.add(node)

            for neighbor in graph.get(node, []):
                if neighbor in visited:
                    continue  # Skip already sorted nodes
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # Check for unsorted nodes (due to cycles)
        remaining_nodes = [node for node in graph if node not in visited]

        # Append remaining nodes in arbitrary order
        sorted_line.extend(remaining_nodes)

        return sorted_line

    ordered_list = []

    for line in input:
        # Build a subgraph for the current line
        graph, in_degree = build_graph_for_line(line, rules)

        # Sort the line using the subgraph
        sorted_line = topological_sort_with_cycles(graph, in_degree)
        ordered_list.append(sorted_line)

    return ordered_list



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

print(len(input))
sum = calculateCorrectMiddleNumbers(input, rules)
print(sum)
ordered_lines = orderLines(input, rules)

sum_two = calculateCorrectMiddleNumbers(ordered_lines, rules)
print(sum_two)
