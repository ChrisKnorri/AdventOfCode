import os
import sys
import math
from pprint import pprint

file_name = os.path.join(os.path.dirname(__file__), "input.txt")

# Parse the input file
with open(file_name, 'r') as file:
    # Read lines, convert each line to a list of characters, and convert each character to an integer
    input = [[int(char) for char in line.strip()] for line in file]

# PART 1

example_input = [1,2,3,4,5,4,3,2,1]
files_and_spaces = []

def convertToFilesAndSpaces(input):
    id = 0
    
    for i, num in enumerate(input):
        if i % 2 == 0:
            while num > 0:
                files_and_spaces.append((id))
                num -= 1
            id += 1
        else:
            while num > 0:
                files_and_spaces.append(('.'))
                num -= 1
                
    return files_and_spaces

def fillSpacesDefragmented(input):
    files_and_spaces = convertToFilesAndSpaces(input)
    tail_index = len(files_and_spaces) - 1
    
    for i, char in enumerate(files_and_spaces):
        if tail_index <= i:
            break 
   
        if char == '.':
            if files_and_spaces[tail_index] != '.':
                files_and_spaces[i] = files_and_spaces[tail_index]
                files_and_spaces[tail_index] = '.'
                tail_index -= 1 
                
            else:
                while files_and_spaces[tail_index] == '.':
                    tail_index -= 1
                files_and_spaces[i] = files_and_spaces[tail_index]
                files_and_spaces[tail_index] = '.'
                tail_index -= 1 
                  
    return files_and_spaces

def fillSpacesDefragmented(input):
    files_and_spaces = convertToFilesAndSpaces(input)
    current_id = 9999  # Start from the highest file ID
    tail_index = len(files_and_spaces) - 1

    # Find all free spans
    free_spans = []
    i = 0
    while i < len(files_and_spaces):
        if files_and_spaces[i] == '.':
            start = i
            while i < len(files_and_spaces) and files_and_spaces[i] == '.':
                i += 1
            free_spans.append((start, i - 1))  # Record start and end of free span
        else:
            i += 1

    while current_id > 0:
        print(f"Processing file ID {current_id}")
        
        # Locate all blocks for the current file ID
        file_blocks = []
        for i in range(tail_index, -1, -1):
            if files_and_spaces[i] == current_id:
                file_blocks.append(i)
            elif file_blocks:
                break  # Stop when leaving the contiguous block

        if not file_blocks:  # Skip if no blocks of current_id are found
            current_id -= 1
            continue

        file_blocks.reverse()  # Order blocks from left to right
        file_length = len(file_blocks)

        # Try to move the file to the leftmost free span
        for start, end in free_spans:
            # Ensure the span is large enough and within the index constraint
            if end - start + 1 >= file_length and start <= min(file_blocks):
                print(f"Moving file ID {current_id} to free span {start}-{start + file_length - 1}")
                for i in range(file_length):
                    files_and_spaces[start + i] = current_id
                for i in file_blocks:
                    files_and_spaces[i] = '.'  # Clear old blocks
                free_spans.remove((start, end))  # Update free spans
                # Add new free span if space remains
                if start + file_length <= end:
                    free_spans.append((start + file_length, end))
                free_spans.sort()  # Keep spans sorted for efficiency
                break

        # Update tail_index and move to next ID
        tail_index = min(file_blocks) - 1
        current_id -= 1

    return files_and_spaces




def calculateChecksum(input):
    files_and_spaces = fillSpacesDefragmented(input)
    print(files_and_spaces[:19])
    # print(f"Final state of files_and_spaces: {''.join(map(str, files_and_spaces))}")

    checksum = 0
    
    for i, char in enumerate(files_and_spaces):
        if char == '.':
            continue
        else:
            checksum += i * char
            
    return checksum

# Flatten the input list
flattened_input = [item for sublist in input for item in sublist]
print(calculateChecksum(flattened_input))