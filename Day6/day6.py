def parse_input() -> list:
    with open('input6.txt', 'r') as f:
        file = f.readlines()
        return [list.strip() for list in file]

# gib Liste von Koordinaten von allen c zurück
def lookup_char_coords(input: list, c: str) -> list:
    list_of_coords = []
    for i, line in enumerate(input):
        y = i
        for j, char in enumerate(line):
            if char == c:
               coords = (j, y)
               list_of_coords.append(coords)
    return list_of_coords

def move_up(coords: tuple) -> tuple:
    x, y = coords
    return (x, y-1)

def move_down(coords: tuple) -> tuple:
    x, y  = coords
    return (x, y+1)

def move_left(coords: tuple) -> tuple:
    x, y = coords
    return (x-1, y)

def move_right(coords: tuple) -> tuple:
    x, y = coords
    return (x+1, y)

def move(coords: tuple, direction: str) -> tuple:
    if direction == "up":
        return move_up(coords)
    if direction == "down":
        return move_down(coords)
    if direction == "left":
        return move_left(coords)
    if direction == "right":
        return move_right(coords)

def is_out_of_bounds(coords: tuple, playground: list) -> bool:
    x, y = coords
    return x < 0 or x >= len(playground) or y < 0 or y >= len(playground[0])

def start_sequence(start: tuple, obstacles: list, input: list) -> None:
    
    position = start
    direction = "up"
    
    distinct_positions = set()
    
    while not is_out_of_bounds(position, input):
        next_position = move(position, direction)
        print(position, next_position, direction)
        
        distinct_positions.add(position)

        if next_position in obstacles:
            print("Hindernis gefunden: ", next_position)
            print("Richtung ändern zu ", change_direction(direction))
            direction = change_direction(direction)
        else:
            position = next_position

            
    print("Out of bounds: ", position)
    return distinct_positions

            
def change_direction(direction: str) -> str:
    if direction == "up":
        return "right"
    if direction == "right":
        return "down"
    if direction == "down":
        return "left"
    if direction == "left":
        return "up"               

def main():
    input = parse_input()
    start = lookup_char_coords(input,'^')[0]
    obstacles = lookup_char_coords(input, '#')
    distinct_locations = start_sequence(start , obstacles, input)
    print(len(distinct_locations))

if __name__ == '__main__':
    main()