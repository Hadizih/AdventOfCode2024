# input parsen
# koordinaten = y,x = zeile + index
# finde X
# prüfen ob rundherum ein M steht [] und positionen speichern
# wenn ja, dann Position M speichern und je nach Richtung weitermachen
# wenn nein, dann weiter

def parse_input() -> list:
    with open('input4small.txt', 'r') as f:
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
    for coords in coordsX:
        y, x = coords
        
            # horizontal rechts
        if x+3 < len(input[y]):
            if input[y][x+1] == 'M':
                if input[y][x+2] == 'A':
                    if input[y][x+3] == 'S':
                        xmas_counter+=1
            # horizontal links
        if x-3 >= 0:
            if input[y][x-1] == 'M':
                if input[y][x-2] == 'A':
                    if input[y][x-3] == 'S':
                        xmas_counter+=1
        if y+3 < len(input):
            # vertikal unten
            if input[y+1][x] == 'M':
                if input[y+2][x] == 'A':
                    if input[y+3][x] == 'S':
                        xmas_counter+=1
            # vertikal oben
        if y-3 >= 0:
            if input[y-1][x] == 'M':
                if input[y-2][x] == 'A':
                    if input[y-3][x] == 'S':
                        xmas_counter+=1
            # diagonal unten rechts
        if y+3 < len(input) and x+3 < len(input[y]):
            if input[y+1][x+1] == 'M':
                if input[y+2][x+2] == 'A':
                    if input[y+3][x+3] == 'S':
                        xmas_counter+=1
            # diagonal oben links
        if y-3 >= 0 and x-3 >= 0:
            if input[y-1][x-1] == 'M':
                if input[y-2][x-2] == 'A':
                    if input[y-3][x-3] == 'S':
                        xmas_counter+=1
            # diagonal unten links
        if y+3 < len(input) and x-3 >= 0:
            if input[y+1][x-1] == 'M':
                if input[y+2][x-2] == 'A':
                    if input[y+3][x-3] == 'S':
                        xmas_counter+=1
            # diagonal oben rechts
        if y-3 >= 0 and x+3 < len(input[y]):
            if input[y-1][x+1] == 'M':
                if input[y-2][x+2] == 'A':
                    if input[y-3][x+3] == 'S':
                        xmas_counter+=1

    return xmas_counter

    
def main():
    input = parse_input()
    coordsX = lookup_X(input)
    print(lookup_XMAS(coordsX, input))

if __name__ == '__main__':
    main()
   