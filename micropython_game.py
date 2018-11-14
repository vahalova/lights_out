from servo import Servos
from machine import Pin, I2C, PWM, reset
from time import sleep
import backend

# construct an I2C bus
i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)
servos = Servos(i2c, 64, min_us=600)


a = 0
b = 45
SIZE = 4
LIGHT = 45
DARK = 135

light_coordinates, dark_coordinates, SIZE = backend.coordinates(SIZE)
def coordinate_dict(light_coordinates):
    coordinate_dict = {}
    for i in range(16):
        coordinate_dict[light_coordinates[i]] = i
    print(coordinate_dict)

def motor(SIZE, light_coordinates, dark_coordinates):
    for coordinate in light_coordinates:
        motor_number = coordinate_dict['coordinate']
        servos.position(motor_number, LIGHT)
        sleep(0.4)
        servos.release(i)
    for coordinate in dark_coordinates:
        motor_number = coordinate_dict['coordinate']
        servos.position(motor_number, DARK)
        sleep(0.4)
        servos.release(i)
