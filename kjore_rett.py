from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *

hub = PrimeHub()
motor_par = MotorPair('A', 'E')
motor_front = Motor('D')
motor_bak = Motor('C')

# Turn on all lights
x = 0
while x < 5:
    y = 0
    while y < 5:
        hub.light_matrix.set_pixel(x, y, 100)
        y = y + 1
    x = x + 1


'''i = 0
brightness = 0
while i < 6:
    x = 0
    y = 0

    while x < 5:
        hub.light_matrix.set_pixel(x, y, brightness)
        x = x + 1

    wait_for_seconds(.3)
    i = i + 1
    brightness = brightness + 20
    print('Lysstyrke: ', brightness)

motor_front.run_to_position(0, direction='shortest path', speed=20)
motor_front.run_to_position(45, direction='shortest path', speed=20)
'''