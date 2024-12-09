from itertools import product
import os
from decimal import Decimal
from pprint import pprint
import string
import math

# Combine all ASCII letters and digits into a single list
ascii_set = list(string.ascii_letters + string.digits)

file_name = os.path.join(os.path.dirname(__file__), "input.txt")

# Parse the input file
with open(file_name, "r") as file:
    input = [list(line.strip()) for line in file]

# PART 1
    
# def findAntennas(matrix, char):
#     antenna_positions = []
#     for i in range(len(matrix)):
#         for j in range(len(matrix[i])):
#             if matrix[i][j] == char:
#                 antenna_positions.append((i, j))
#     return antenna_positions

# def calculateAntinodes(matrix, antenna_positions):
#     possible_antinodes = []
#     rows = len(matrix)
#     cols = len(matrix[0]) if rows > 0 else 0

#     for i, current in enumerate(antenna_positions):
#         remaining_antennas = antenna_positions[:i] + antenna_positions[i + 1:]

#         for temp in remaining_antennas:
#             # Differences in rows and columns
#             dx = temp[0] - current[0]
#             dy = temp[1] - current[1]

#             # Generate potential antinodes based on proportional distance
#             antinode_position_1 = (current[0] - dx, current[1] - dy)  # Twice as far in reverse direction
#             antinode_position_2 = (temp[0] + dx, temp[1] + dy)        # Twice as far in the forward direction

#             # Check if they are within bounds
#             if 0 <= antinode_position_1[0] < rows and 0 <= antinode_position_1[1] < cols:
#                 possible_antinodes.append(antinode_position_1)
#             if 0 <= antinode_position_2[0] < rows and 0 <= antinode_position_2[1] < cols:
#                 possible_antinodes.append(antinode_position_2)

#     return list(set(possible_antinodes))  # Deduplicate the list     

# def countAntinodes(matrix, char_set):
#     antinodes = []
    
#     for char in char_set:
#         antennas = findAntennas(matrix, char)
#         antinodes.append(calculateAntinodes(matrix, antennas))
    
#     antinodes_flattened = [item for sublist in antinodes for item in sublist]
#     distinct_antinodes = list(set(antinodes_flattened))
    
#     return distinct_antinodes
    
# antinodes = countAntinodes(input, ascii_set)
# no_of_antinodes = len(antinodes)
# print(no_of_antinodes)

# PART 2

def findAntennas(matrix, char):
    antenna_positions = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == char:
                antenna_positions.append((i, j))
    return antenna_positions

def calculateAntinodes(matrix, antenna_positions):
    possible_antinodes = set()  # Use a set to avoid duplicates
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0

    for i, current in enumerate(antenna_positions):
        remaining_antennas = antenna_positions[:i] + antenna_positions[i + 1:]

        # Self-antinode check: if the current antenna is in line with at least two others
        in_line_count = 0

        for temp in remaining_antennas:
            # Differences in rows and columns
            dx = temp[0] - current[0]
            dy = temp[1] - current[1]

            # Normalize dx and dy to a unit vector (direction)
            gcd = abs(dx) if dy == 0 else abs(dy) if dx == 0 else abs(math.gcd(dx, dy))
            dx //= gcd
            dy //= gcd

            # Find all points along the line passing through `current` and `temp`
            starter_node = current
            while 0 <= starter_node[0] < rows and 0 <= starter_node[1] < cols:
                starter_node = (starter_node[0] - dx, starter_node[1] - dy)
            starter_node = (starter_node[0] + dx, starter_node[1] + dy)

            # Generate potential antinodes along the line
            aligned_nodes = []
            while 0 <= starter_node[0] < rows and 0 <= starter_node[1] < cols:
                aligned_nodes.append(starter_node)
                starter_node = (starter_node[0] + dx, starter_node[1] + dy)

            # Count valid points and add them to possible antinodes
            in_line_count += 1
            for node in aligned_nodes:
                possible_antinodes.add(node)

        # Add the current antenna as an antinode if it aligns with at least two others
        if in_line_count >= 2:
            possible_antinodes.add(current)

    return possible_antinodes


def countAntinodes(matrix, char_set):
    antinodes = set()  # Use a set for global deduplication
    
    for char in char_set:
        antennas = findAntennas(matrix, char)
        if len(antennas) > 1:  # Only process if there are at least two antennas
            antinodes.update(calculateAntinodes(matrix, antennas))
    
    return len(antinodes)


# Run the calculation
antinodes_count = countAntinodes(input, ascii_set)
print(antinodes_count)
