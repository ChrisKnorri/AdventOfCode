import os

# Get input from file
current_dir = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(current_dir, "input.txt"), "r") as file:
    matrix = [list(line.strip()) for line in file]

# PART 1

# # FUNCTIONS

# def findGuard(matrix):
#     for i in range(len(matrix)):
#         for j in range(len(matrix[i])):
#             if matrix[i][j] == '^' or matrix[i][j] == '<' or matrix[i][j] == '>' or matrix[i][j] == 'v':
#                 return i, j

# def redirectGuard(pose):
#     if pose == '^':
#         return 0, 1, '>'
#     elif pose == '>':
#         return 1, 0, 'v'
#     elif pose == 'v':
#         return 0, -1, '<'
#     elif pose == '<':
#         return -1, 0, '^'   

# def moveGuard(matrix, x, y, dx, dy, pose):
#     rows = len(matrix)
#     cols = len(matrix[0]) if rows > 0 else 0
    
#     # MOVE THROUGH THE MATRIX WHILE GUARD's POSITION IS STILL VALID
#     while 0 <= x + dx < rows and 0 <= y + dy < cols:
#         matrix[x][y] = 'X'                              # Mark current cell
#         x += dx                                         # Change guard's position
#         y += dy
        
#         if matrix[x + dx][y + dy] == '#':               # If guard hits an obstacle, redirect
#             dx, dy, pose = redirectGuard(pose)             
#     # STOP IF GUARD WOULD EXIT THE MATRIX
    
#     # MARK LAST CELL BEFORE LEAVING
#     matrix[x][y] = 'X'
    
#     match pose:
#             case '^':
#                 direction = "NORTH"
#             case '<':
#                 direction = "WEST"
#             case '>':
#                 direction = "EAST"
#             case 'v':
#                 direction = "SOUTH"
#             case _:
#                 pass
    
#     print(matrix)  
#     print(rows, cols)     
#     print(f"Guard exiting towards {direction}. Last cell: ({x},{y})")

# def calculateDistinctPositions(matrix):
    
#     distinct_position_counter = 0
    
#     for i in range(len(matrix)):
#         for j in range(len(matrix[i])):
#             if matrix[i][j] == 'X':
#                 distinct_position_counter += 1
    
#     return distinct_position_counter

# def processGuardPatrolRoute(matrix):
#     guard_x, guard_y = findGuard(matrix)  
#     guard_pose = matrix[guard_x][guard_y]
#     dx, dy = 0, 0
    
#     match guard_pose:
#             case '^':
#                 dx, dy = -1, 0
#             case '<':
#                 dx, dy = 0, -1
#             case '>':
#                 dx, dy = 0, 1
#             case 'v':
#                 dx, dy = 1, 0
#             case _:
#                 pass
            
#     moveGuard(matrix, guard_x, guard_y, dx, dy, guard_pose)       


    
# GUARD_STARTING_X, GUARD_STARTING_Y = findGuard(matrix)
# print(f"Guard Starting at ({GUARD_STARTING_X}, {GUARD_STARTING_Y}). Pose: {matrix[GUARD_STARTING_X][GUARD_STARTING_Y]})")

# processGuardPatrolRoute(matrix)
# num_of_Xs = calculateDistinctPositions(matrix)
# print(num_of_Xs)

# # # Filepath to save the output
# # output_file = current_dir + "/output.txt"

# # # Writing the matrix to the file
# # with open(output_file, "w") as file:
# #     for row in matrix:
# #         file.write("".join(row) + "\n")  # Join characters in each row and add a newline

# # print(f"Matrix written to {output_file}")


# PART 2

# FUNCTIONS

def findGuard(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == '^' or matrix[i][j] == '<' or matrix[i][j] == '>' or matrix[i][j] == 'v':
                return i, j

def redirectGuard(pose):
    if pose == '^':
        return 0, 1, '>'
    elif pose == '>':
        return 1, 0, 'v'
    elif pose == 'v':
        return 0, -1, '<'
    elif pose == '<':
        return -1, 0, '^'   

def markCell(matrix, x, y, pose):
        if pose == '<':
            matrix[x][y] = '<'
        elif pose == '^':
            matrix[x][y] = '^'
        elif pose == '>':
            matrix[x][y] = '>'
        elif pose == 'v':
            matrix[x][y] = 'v'

def checkForPossibleLoop(matrix, rows, cols, x, y, pose):
    if pose == '<':
        while 0 <= x < rows:
            if matrix[x][y] == '^':
                return True
            elif matrix[x][y] == '+':
                if matrix[x-1][y] == '^':
                    return True
            elif matrix[x][y] == '#':
                return False
            x -= 1
        return False
                
    elif pose == '>':
        while 0 <= x < rows:
            if matrix[x][y] == 'v':
                return True
            elif matrix[x][y] == '+':
                if matrix[x+1][y] == 'v':
                    return True
            elif matrix[x][y] == '#':
                return False
            x += 1
        return False
    
    elif pose == '^':
        while 0 <= y < cols:
            if matrix[x][y] == '>':
                return True
            elif matrix[x][y] == '+':
                if matrix[x][y+1] == '>':
                    return True
            elif matrix[x][y] == '#':
                return False
            y += 1
        return False
    
    elif pose == 'v':
        while 0 <= y < cols:
            if matrix[x][y] == '<':
                return True
            elif matrix[x][y] == '+':
                if matrix[x][y-1] == '<':
                    return True
            elif matrix[x][y] == '#':
                return False
            y -= 1
        return False 
        
def moveGuardAndCount(matrix, x, y, dx, dy, pose):
          
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    num_of_possible_loops = 0
    
    # MOVE THROUGH THE MATRIX WHILE GUARD's POSITION IS STILL VALID
    while 0 <= x + dx < rows and 0 <= y + dy < cols:
      
        if matrix[x + dx][y + dy] == '#':               # If guard hits an obstacle, redirect
            dx, dy, pose = redirectGuard(pose)
            matrix[x][y] = '+'       
        elif checkForPossibleLoop(matrix, rows, cols, x, y, pose):  # If Loop is detected, mark a possible junction and move one step further.
            matrix[x][y] = '+'
            x += dx
            y += dy
            num_of_possible_loops += 1    
        else:
            markCell(matrix, x, y, pose)
            x += dx                                         # Change guard's position
            y += dy
    # STOP IF GUARD WOULD EXIT THE MATRIX
    
    # MARK LAST CELL BEFORE LEAVING
    markCell(matrix, x, y, pose)
    
    match pose:
            case '^':
                direction = "NORTH"
            case '<':
                direction = "WEST"
            case '>':
                direction = "EAST"
            case 'v':
                direction = "SOUTH"
            case _:
                pass
    
    # print(matrix)  
    print(rows, cols)     
    print(f"Guard exiting towards {direction}. Last cell: ({x},{y})")
    print(f"Number of possible loop causing obstacles: {num_of_possible_loops}") 

def calculateDistinctPositions(matrix):
    
    distinct_position_counter = 0
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 'X':
                distinct_position_counter += 1
    
    return distinct_position_counter

def processGuardPatrolRoute(matrix):
    GUARD_STARTING_X, GUARD_STARTING_Y = findGuard(matrix)  
    guard_pose = matrix[GUARD_STARTING_X][GUARD_STARTING_Y]
    dx, dy = 0, 0
    
    print(f"Guard Starting at ({GUARD_STARTING_X}, {GUARD_STARTING_Y}). Pose: {guard_pose})")
    
    match guard_pose:
            case '^':
                dx, dy = -1, 0
            case '<':
                dx, dy = 0, -1
            case '>':
                dx, dy = 0, 1
            case 'v':
                dx, dy = 1, 0
            case _:
                pass
            
    moveGuardAndCount(matrix, GUARD_STARTING_X, GUARD_STARTING_Y, dx, dy, guard_pose)       

processGuardPatrolRoute(matrix)

# Filepath to save the output
output_file = current_dir + "/output_2.txt"

# Writing the matrix to the file
with open(output_file, "w") as file:
    for row in matrix:
        file.write("".join(row) + "\n")  # Join characters in each row and add a newline

print(f"Matrix written to {output_file}")

def simulate_guard(matrix, obstruction=None):
    rows, cols = len(matrix), len(matrix[0])
    visited_states = set()
    guard_x, guard_y = findGuard(matrix)
    guard_pose = matrix[guard_x][guard_y]

    # Define directions
    directions = {
        "^": (-1, 0),
        "v": (1, 0),
        "<": (0, -1),
        ">": (0, 1)
    }

    direction_cycle = ["^", ">", "v", "<"]

    def turn_right(pose):
        return direction_cycle[(direction_cycle.index(pose) + 1) % 4]

    # Place the obstruction temporarily, if any
    if obstruction:
        ox, oy = obstruction
        matrix[ox][oy] = "#"

    # Simulate guard's movement
    x, y, pose = guard_x, guard_y, guard_pose
    while (x, y, pose) not in visited_states:
        visited_states.add((x, y, pose))

        dx, dy = directions[pose]
        nx, ny = x + dx, y + dy

        if 0 <= nx < rows and 0 <= ny < cols and matrix[nx][ny] != "#":
            x, y = nx, ny
        else:
            pose = turn_right(pose)

        # Guard exits the grid
        if not (0 <= x < rows and 0 <= y < cols):
            break

    # Remove the obstruction
    if obstruction:
        ox, oy = obstruction
        matrix[ox][oy] = "."

    # Check for loop: revisit same position and direction
    return (x, y, pose) in visited_states


def count_valid_obstruction_positions(matrix):
    rows, cols = len(matrix), len(matrix[0])
    loop_positions = 0

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == ".":
                if simulate_guard(matrix, obstruction=(i, j)):
                    loop_positions += 1

    return loop_positions


# Call the function and print the result
result = count_valid_obstruction_positions(matrix)
print("Number of valid obstruction positions causing loops:", result)
