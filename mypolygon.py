__author__ = 'Derek'

from swampy.TurtleWorld import *
import math

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.1
print bob

def square(t, l):
    for i in range(4):
        fd(t, l)
        lt(t)

def polyline(t, n, length, angle):
    for i in range(n):
        fd(t, length)
        lt(t, angle)

def polygon(t, n, length):
    angle = 360/n
    polyline(t, n, length, angle)

def arc(t, r, angle):
    arc_length = (2 * math.pi * r) * angle/360
    n = int(arc_length/3) + 1

    step_length = arc_length/n
    step_angle = float(angle/n)

    polyline(t, n, step_length, step_angle)

arc(bob, 100, 90)



wait_for_user()

