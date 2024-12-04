
def parse_input() -> list:
    with open('input4.txt', 'r') as f:
        file = f.readlines()
        return [list.strip() for list in file]


def lookup_char_coords(input: list, c: str) -> list:
    list_of_coords = []
    for i, line in enumerate(input):
        y = i
        for j, char in enumerate(line):
            if char == c:
               coords = (y, j)
               list_of_coords.append(coords)
    return list_of_coords


def lookup_XMAS(coordsX: list, input:list) -> int:
    
    xmas_counter = 0

    directions = [
        (0, 1),   # horizontal rechts
        (0, -1),  # horizontal links
        (1, 0),   # vertikal unten
        (-1, 0),  # vertikal oben
        (1, 1),   # diagonal unten rechts
        (-1, -1), # diagonal oben links
        (1, -1),  # diagonal unten links
        (-1, 1)   # diagonal oben rechts    
    ]
    # mehr pythonic by AI
    for y, x in coordsX:
        for dy, dx in directions:
            # Prüfe, ob alle Indizes im gültigen Bereich liegen
            if 0 <= y + 3 * dy < len(input) and 0 <= x + 3 * dx < len(input[y]):
                # Überprüfe die "XMAS"-Reihenfolge
                if (
                    input[y + dy][x + dx] == 'M' and
                    input[y + 2 * dy][x + 2 * dx] == 'A' and
                    input[y + 3 * dy][x + 3 * dx] == 'S'
                ):
                    xmas_counter += 1
    return xmas_counter

def lookup_x_mas(coordsA: list, input: list) -> int:
    x_mas_mas_counter = 0
    directions: list = [
        (-1, -1), # diagonal oben links
        (1, 1),   # diagonal unten rechts
        (-1, 1),  # diagonal oben rechts
        (1, -1)   # diagonal unten links
    ]

    for y, x in coordsA:
        x_mas_counter = 0
        for dy, dx in directions:
            if 0 <= y + dy*-1 < len(input) and 0 <= x + dx*-1 < len(input[y]) and 0 <= y + dy < len(input) and 0 <= x + dx < len(input[y]):
                if (input[y + dy][x + dx] == 'M' and input[y + dy*-1][x + dx*-1] == 'S'):
                    x_mas_counter += 1
        if x_mas_counter >= 2:
            x_mas_mas_counter += 1

    return x_mas_mas_counter

def main():
    input = parse_input()
    coordsX = lookup_char_coords(input, 'X')
    coordsA = lookup_char_coords(input, 'A')
    print(f"Part1 - XMAS: {lookup_XMAS(coordsX, input)}")
    print(f"Part2 - X-MAS: {lookup_x_mas(coordsA, input)}")

if __name__ == '__main__':
    main()
   