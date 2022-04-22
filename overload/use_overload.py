# -*- coding: utf-8 -*-
from overload import overload


@overload
def area(length, breadth):
    return length * breadth


@overload
def area(radius):
    import math
    return math.pi * radius ** 2


@overload
def area(length, breadth, height):
    return 2 * (length * breadth + breadth * height + height * length)


@overload
def volume(length, breadth, height):
    return length * breadth * height


@overload
def area(length, breadth, height):
    return length + breadth + height


@overload
def area():
    return 0


print(f"area of cuboid with dimension (4, 3, 6) is: {area(4, 3, 6)}")
print(f"area of rectangle with dimension (7, 2) is: {area(7, 2)}")
print(f"area of circle with radius 7 is: {area(7)}")
print(f"area of nothing is: {area()}")
print(f"volume of cuboid with dimension (4, 3, 6) is: {volume(4, 3, 6)}")
