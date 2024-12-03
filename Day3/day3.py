import re

# get the input from the file 
def get_input():
    with open('input3.txt', 'r') as f:
        return f.read()
    
# extract the numbers from the mul instruction
def extract_valid_mul(text: str) -> list:
    return re.findall(r'mul\((\d+),(\d+)\)', text)

# calculate the sum of the product of the two numbers in the instructions
def calculate_instructions(instructions: list) -> int:
    return sum(int(a)*int(b) for a,b in instructions)

# extract the valid instructions from the text between do() and don't()
def extract_valid_instructions(text: str) -> list:
    valid_parts = re.findall(r"(?:don't\(\)|do\(\)|mul\(\d{1,3},\s*\d{1,3}\))", text)
    valid_instructions = []

    is_active = True;    

    for part in valid_parts:
        if part == "do()":
            is_active = True
        elif part == "don't()":
            is_active = False
        else:
            if is_active:
                part = part[4:-1].split(',')
                valid_instructions.append(part)           
        
    return valid_instructions
                           
                        

if __name__ == '__main__':
    input = get_input()
    instructions = extract_valid_mul(input)
    valid_instructions = extract_valid_instructions(input)
    print(calculate_instructions(valid_instructions))