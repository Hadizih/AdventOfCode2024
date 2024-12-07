# Adjusting logic to include full left-to-right evaluation, specifically ensuring concatenation works correctly
from itertools import product

def evaluate_expression_v2(nums, operators):
    result = nums[0]
    for num, op in zip(nums[1:], operators):
        if op == "||":
            result = int(str(result) + str(num))  # Concatenate numbers as integers
        elif op == "+":
            result += num  # Addition
        elif op == "*":
            result *= num  # Multiplication
    return result




def get_input():
    with open("input7.txt") as f:
        return f.read()


def parse_input(input_data):
    equations = []
    for line in input_data.strip().split("\n"):
        target, numbers = line.split(":")
        target = int(target.strip())
        nums = list(map(int, numbers.split()))
        equations.append((target, nums))
    return equations


def calculate_calibration_sum_v2(input_data):
    equations = parse_input(input_data)
    total = 0

    for target, nums in equations:
        num_count = len(nums) - 1  # Number of operators needed
        valid = False

        # Generate all possible combinations of operators
        for operators in product(["+", "*", "||"], repeat=num_count):
            try:
                if evaluate_expression_v2(nums, operators) == target:
                    valid = True
                    break  # Stop if any valid combination is found
            except Exception:
                continue

        if valid:
            total += target  # Add the target value if valid

    return total

# Recalculate with updated logic
input_data =get_input()
correct_result = calculate_calibration_sum_v2(input_data)
print(correct_result)  # 208
