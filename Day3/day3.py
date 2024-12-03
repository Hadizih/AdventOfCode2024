import re

def get_input():
    with open('input3.txt', 'r') as f:
        return f.read()
    
def extract_valid_mul(text: str) -> list:
    return re.findall(r'mul\((\d+),(\d+)\)', text)

def calculate_instructions(instructions: list) -> int:
    return sum(int(a)*int(b) for a,b in instructions)


if __name__ == '__main__':
    input = get_input()
    instructions = extract_valid_mul(input)
    print(calculate_instructions(instructions))
