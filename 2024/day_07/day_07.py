from itertools import product
import os
from decimal import Decimal


file_name = os.path.join(os.path.dirname(__file__), "input.txt")

def create_operator_sets(num, operators):
    return list(product(operators, repeat=num))

def left_to_right_eval(numbers, operators):
    result = numbers[0]
    for i, op in enumerate(operators):
        if op == '+':
            result += numbers[i + 1]
        elif op == '*':
            result *= numbers[i + 1]
        elif op == '||':
            result = str(result) + str(numbers[i + 1])
            result = int(result)
    return result

  
def run_possible_operations(input, operators):
    total_sum = 0
    
    for line in input:
        result = int(line[0])  # The test value
        numbers = list(map(int, line[1:]))  # Remaining numbers
        num_of_operators = len(numbers) - 1
        possible_solutions = create_operator_sets(num_of_operators, operators)
        
        for solution in possible_solutions:
            # Construct the expression
            # expression = "".join(f"{n}{op}" for n, op in zip(numbers, solution)) + str(numbers[-1])
            # temp_result = eval(expression, {"__builtins__": None}, {"Decimal": Decimal})
            
            # # Debugging output
            # print(f"Testing expression: {expression} = {temp_result} (Expected: {result})")
            
            temp_result = left_to_right_eval(numbers, solution)
            
            if temp_result == result:
                total_sum += result
                break  # Stop checking other operator combinations once matched
                        
    print("Total Calibration Sum:", total_sum)

# Parse the input file
with open(file_name, "r") as file:
    input_data = [line.strip().split() for line in file]
    for line in input_data:
        line[0] = line[0].strip(':')

operators = ['+', '*', '||']
run_possible_operations(input_data, operators)
