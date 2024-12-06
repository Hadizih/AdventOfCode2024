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
    # counts position of the circle in which the robot is stuck
    circle_counter = 0
    circle_detection = 0
    max_iterations = 5000
    iterations = 0
    

    while not is_out_of_bounds(position, input):
        print(f"Position: {position}, Direction: {direction}")
        if iterations > max_iterations:
            print("Max iterations reached")
            break
        next_position = move(position, direction)
        
        if position in distinct_positions:
            circle_counter += 1
            
        distinct_positions.add(position)

        if next_position in obstacles:
            direction = change_direction(direction)
        else:
            position = next_position

        if circle_counter == 10:
           circle_detection += 1
        
        iterations += 1
           

    return distinct_positions, circle_detection        


            
def change_direction(direction: str) -> str:
    if direction == "up":
        return "right"
    if direction == "right":
        return "down"
    if direction == "down":
        return "left"
    if direction == "left":
        return "up"               

def create_new_map(input: list, new_obstacle: tuple) -> list:
    x,y = new_obstacle

    new_input = input[:]

    new_input[y] = new_input[y][:x] + '#' + new_input[y][x+1:]
    return new_input

def start_sequence(start: tuple, obstacles: list, input: list) -> None:
    
    position = start
    direction = "up"
    
    distinct_positions = set()
    # counts position of the circle in which the robot is stuck
    circle_detection = 0
    max_iterations = 10000
    iterations = 0
    

    while not is_out_of_bounds(position, input):
        
        if iterations > max_iterations:
            print("Max iterations reached")
            circle_detection += 1
            break

        next_position = move(position, direction)
        
        distinct_positions.add(position)

        if next_position in obstacles:
            direction = change_direction(direction)
        else:
            position = next_position

        iterations += 1
           

    return distinct_positions, circle_detection      
  
def calculate_new_obstacle_positions(input: list) -> int:
    total_circles = 0  
    maps_with_circles = 0  

    for y, row in enumerate(input):
        for x, point in enumerate(row):
            new_obstacle = (x, y)
            print(f"New Obstacle: {new_obstacle}")
            start = lookup_char_coords(input, '^')[0]
            

            if new_obstacle == start: 
                continue

            
            new_input = create_new_map(input, new_obstacle)
            obstacles = lookup_char_coords(new_input, '#')
            
            distinct_locations, circle = start_sequence(start, obstacles, new_input)

            if circle > 0:
                
                maps_with_circles += 1  
                total_circles += circle  

    return maps_with_circles


def main():

    input = parse_input()
    start = lookup_char_coords(input,'^')[0]
    
    obstacles = lookup_char_coords(input, '#')
    ##p1
    distinct_locations, circle = start_sequence(start , obstacles, input)
    print(f"Part1 {len(distinct_locations)}")
    

    ##p2
    obstacle_positions = calculate_new_obstacle_positions(input)
    print(f"Positions Total: {obstacle_positions}")

if __name__ == '__main__':
    main()  