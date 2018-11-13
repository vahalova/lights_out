from servo import Servos
from machine import Pin, I2C
from time import sleep
# construct an I2C bus
i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)
servos = Servos(i2c, 64, min_us=600)

a = 0
b = 45

if b >= 0 and b <= 180:
    for i in range(16):
        servos.position(i, b)
        sleep(0.4)
        servos.release(i)

else:
    print('Máš tam překlep!')
