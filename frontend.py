import pyglet
import backend


light = 'ground.png'
dark = 'hole.png'
SQUARE_SIZE = 64

def input_size(input=input):
    SIZE = int(input('The width of the playing area (between 2 and 30): '))
    while not is_valid_size(SIZE):
        print('The size must be between 2 and 30')
        SIZE = int(input('The width of the playing area (between 2 and 30): '))
    return SIZE

def is_valid_size(SIZE):
    if SIZE > 1 and SIZE <= 30:
        return True

def check_win(dark_coordinates):
    if len(dark_coordinates) == 0:
        print('You won!!')

def draw(SIZE, light_coordinates, dark_coordinates):
    window = pyglet.window.Window(SIZE*SQUARE_SIZE, SIZE*SQUARE_SIZE)

    def click(x, y, button, mod):
        coordinate_x = x//SQUARE_SIZE
        coordinate_y = y//SQUARE_SIZE
        click_coordinate = (coordinate_x, coordinate_y)
        backend.cross_switch(click_coordinate, light_coordinates, dark_coordinates, SIZE)
        check_win(dark_coordinates)

    def draw_imgs():
        window.clear()
        for coordinate in light_coordinates:
            img = pyglet.image.load(light)
            #adding an image to the coordinates
            square = pyglet.sprite.Sprite(img, x=coordinate[0] * SQUARE_SIZE, y=coordinate[1] * SQUARE_SIZE)
            square.draw()
        for coordinate in dark_coordinates:
            img = pyglet.image.load(dark)
            #adding an image to the coordinates
            square = pyglet.sprite.Sprite(img, x=coordinate[0] * SQUARE_SIZE, y=coordinate[1] * SQUARE_SIZE)
            square.draw()
    window.push_handlers(on_draw = draw_imgs, on_mouse_press=click)

    pyglet.app.run()
