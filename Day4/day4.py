# input parsen
# koordinaten = y,x = zeile + index
# finde X
# prüfen ob rundherum ein M steht [] und positionen speichern
# wenn ja, dann Position M speichern und je nach Richtung weitermachen
# wenn nein, dann weiter

def parse_input() -> list:
    with open('input4.txt', 'r') as f:
        file = f.readlines()
        return [list.strip() for list in file]


def lookup_X(input: list) -> list:
    coordsX = []
    for i, line in enumerate(input):
        y = i
        for j, char in enumerate(line):
            if char == 'X':
               coords = (y, j)
               coordsX.append(coords)
    return coordsX


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

    
def main():
    input = parse_input()
    coordsX = lookup_X(input)
    print(lookup_XMAS(coordsX, input))

if __name__ == '__main__':
    main()
   