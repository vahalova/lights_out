import random

def coordinates(SIZE):
    light_coordinates = []
    dark_coordinates = []
    for y in range(SIZE):
        for x in range(SIZE):
            light_coordinates.append((x,y))
    # print(light_coordinates)
    return light_coordinates, dark_coordinates, SIZE

def starting_positions(light_coordinates, dark_coordinates, SIZE):
    # print('light_coordinates',light_coordinates)
    starting_list = []
    while len(starting_list) == 0:
        for coordinate in light_coordinates:
            for _ in range(random.randrange(5)):
                    starting_list.append(coordinate)
    random.shuffle(starting_list)
    # print('starting_list', starting_list)
    for click_coordinate in starting_list:
        # print('click_coordinate',click_coordinate )
        change(click_coordinate, light_coordinates, dark_coordinates, SIZE)

def change(click_coordinate, light_coordinates, dark_coordinates, SIZE):
    coordinate_x, coordinate_y = click_coordinate
    change_list = [(coordinate_x, coordinate_y)]
    if coordinate_x + 1 <= (SIZE - 1):
        change_list.append((coordinate_x + 1, coordinate_y))
    if coordinate_x - 1 >= (0):
        change_list.append((coordinate_x - 1, coordinate_y))
    if coordinate_y + 1 <= (SIZE-1):
        change_list.append((coordinate_x, coordinate_y + 1))
    if coordinate_y - 1 >= (0):
        change_list.append((coordinate_x, coordinate_y - 1))
    for coordinate in change_list:
        if coordinate in light_coordinates:
            light_coordinates.remove(coordinate)
            dark_coordinates.append(coordinate)
        else:
            light_coordinates.append(coordinate)
            dark_coordinates.remove(coordinate)
    check_winnings(dark_coordinates)
    # print('light_coordinates, dark_coordinates', light_coordinates, dark_coordinates)

def check_winnings(dark_coordinates):
    if len(dark_coordinates) == 0:
        print('You won!!')
