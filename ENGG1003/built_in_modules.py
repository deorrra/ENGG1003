import math
def triangle(x, y, angle):
    x = 10.0            # horiontal length
    y = 10.0            # vertical length
    angle = math.atan(x/y)   # arctan
    return (angle/math.pi) * 180 #conversion from rad to deg