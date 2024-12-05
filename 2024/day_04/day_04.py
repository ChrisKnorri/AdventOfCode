import os
import re
from pprint import pprint

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Define the file path relative to the script's directory
file_path = os.path.join(current_dir, 'input.txt')

# Open the file and read the matrix
with open(file_path, 'r') as file:
    # Read lines and convert each line to a list of characters
    matrix = [list(line.strip()) for line in file]

# XMAS_cnt = 0

# def count_word_occurrences(matrix, word):
#     rows = len(matrix)
#     cols = len(matrix[0]) if rows > 0 else 0
#     word_len = len(word)
#     reverse_word = word[::-1]
#     directions = [
#         (0, 1),   # Right

#         (1, 0),   # Down

#         (1, 1),   # Diagonal down-right
#         (1, -1),  # Diagonal down-left

#     ]
#     count = 0

#     for i in range(rows):
#         for j in range(cols):
#             for di, dj in directions:
#                 # Check forward direction
#                 if all(
#                     0 <= i + k * di < rows and
#                     0 <= j + k * dj < cols and
#                     matrix[i + k * di][j + k * dj] == word[k]
#                     for k in range(word_len)
#                 ):
#                     count += 1
#                 # Check backward direction
#                 if all(
#                     0 <= i + k * di < rows and
#                     0 <= j + k * dj < cols and
#                     matrix[i + k * di][j + k * dj] == reverse_word[k]
#                     for k in range(word_len)
#                 ):
#                     count += 1

#     return count

# # Read the input file and create the matrix
# with open(file_path, 'r') as file:
#     matrix = [list(line.strip()) for line in file]

# # Count occurrences of 'XMAS'
# total_occurrences = count_word_occurrences(matrix, 'XMAS')
# print(total_occurrences)



def count_word_occurrences(matrix, word):
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    word_len = len(word)
    count = 0

    directions_pairs = [
    ((1, 1), (1, -1)),   # down-right and down-left
    ]

    for i in range(rows):
        for j in range(cols):
            for (di1, dj1), (di2, dj2) in directions_pairs:
                try:
                    # Check if first word is valid
                    if all(
                        0 <= i + k * di1 < rows and
                        0 <= j + k * dj1 < cols and
                        matrix[i + k * di1][j + k * dj1] == word[k]
                        for k in range(word_len)
                    ):
                        # Check if second crossing word is valid
                        if all(
                            0 <= i + k * di2 < rows and
                            0 <= j+2 + k * dj2 < cols and
                            matrix[i + k * di2][j+2 + k * dj2] == word[k]
                            for k in range(word_len)
                        ):
                            count += 1
                except IndexError:
                    pass

    return count

def rotate_matrix_90_degrees(matrix):
    return [list(row)[::-1] for row in zip(*matrix)]

# Read the matrix
with open(file_path, 'r') as file:
    matrix = [list(line.strip()) for line in file]

# Total count by checking in all rotations
total_count = 0
current_matrix = matrix
for _ in range(4):  # 4 rotations cover all directions
    total_count += count_word_occurrences(current_matrix, 'MAS')
    current_matrix = rotate_matrix_90_degrees(current_matrix)

print(total_count)