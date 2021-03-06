from os import urandom


def coordinates(SIZE):
    light_coordinates = []
    dark_coordinates = []
    for y in range(SIZE):
        for x in range(SIZE):
            light_coordinates.append((x,y))
    return light_coordinates, dark_coordinates, SIZE

def starting_positions(light_coordinates, dark_coordinates, SIZE):
    starting_list = []
    while len(starting_list) <= 3:
        for coordinate in light_coordinates:
            for _ in range(urandom(1)[0] % 5):
                    starting_list.append(coordinate)
    n = len(starting_list)
    shuffle_list = []
    for r in urandom(n):
        chosen = starting_list[r%n]
        del starting_list[r%n]
        shuffle_list.append(chosen)
        n -= 1
    starting_list.extend(shuffle_list)
    for click_coordinate in starting_list:
        cross_switch(click_coordinate, light_coordinates, dark_coordinates, SIZE)

def cross_switch(click_coordinate, light_coordinates, dark_coordinates, SIZE):
    coordinate_x, coordinate_y = click_coordinate
    cross_switch_list = [(coordinate_x, coordinate_y)]
    if coordinate_x + 1 <= (SIZE - 1):
        cross_switch_list.append((coordinate_x + 1, coordinate_y))
    if coordinate_x - 1 >= (0):
        cross_switch_list.append((coordinate_x - 1, coordinate_y))
    if coordinate_y + 1 <= (SIZE-1):
        cross_switch_list.append((coordinate_x, coordinate_y + 1))
    if coordinate_y - 1 >= (0):
        cross_switch_list.append((coordinate_x, coordinate_y - 1))
    for coordinate in cross_switch_list:
        if coordinate in light_coordinates:
            light_coordinates.remove(coordinate)
            dark_coordinates.append(coordinate)
        else:
            light_coordinates.append(coordinate)
            dark_coordinates.remove(coordinate)
    return light_coordinates, dark_coordinates
