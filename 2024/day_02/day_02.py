import os
from pprint import pprint


with open('/home/knorri/projects/AOC24/day_02/lists.txt', 'r') as file:
    lists_file = file.readlines()
    
    lists = [list(map(int, line.split())) for line in lists_file]
    
safe_cnt = 0
    
def is_safe(sequence):
    """Check if a sequence is safe without removing any levels."""
    direction = None
    for i in range(1, len(sequence)):
        difference = sequence[i] - sequence[i - 1]
        if abs(difference) < 1 or abs(difference) > 3:
            return False
        if direction is None:  # Set direction on the first comparison
            direction = "increasing" if difference > 0 else "decreasing"
        elif (direction == "increasing" and difference < 0) or \
             (direction == "decreasing" and difference > 0):
            return False
    return True

safe_cnt = 0

for line in lists:
    if is_safe(line):
        safe_cnt += 1
        continue

    # Try removing each level to see if it becomes safe
    dampened_safe = False
    for i in range(len(line)):
        test_sequence = line[:i] + line[i + 1:]
        if is_safe(test_sequence):
            dampened_safe = True
            break

    if dampened_safe:
        safe_cnt += 1

print(f"Number of safe reports: {safe_cnt}")
            
            
                
            
             
            
