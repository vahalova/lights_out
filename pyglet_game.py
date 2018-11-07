import backend
import frontend

def main(input=input):
    SIZE = frontend.input_size()
    light_coordinates, dark_coordinates, SIZE = backend.coordinates(SIZE)
    backend.starting_positions(light_coordinates, dark_coordinates, SIZE)
    frontend.draw(SIZE, light_coordinates, dark_coordinates)


if __name__ == '__main__':
    main()
