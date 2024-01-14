'''
CIS 211

Author: Ernest Ho

Credits:

Description: A code for finding the area & volume of a cylinder and Cuboid
by calling on subclasses and superclasses.

'''
#File: Shape3D.py
import math


class Shape3D:

    def __init__(self):
        raise NotImplementedError("Abstract class cannot be instantiated")

    def volume(self) -> float:
        raise NotImplementedError("Not implemented for abstract class")

    def area(self) -> float:
        raise NotImplementedError("Not implemented for abstract class")

    def print_info(self):
        area = self.area()
        volume = self.volume()
        print(f"Area: {area} Volume: {volume}")


class Cylinder(Shape3D):
    """Calls on Shape3D to print the area & volume
    or return an invalid argument"""
    def __init__(self, r: int, h: int):
        self.r = r
        self.h = h

    def volume(self):
        """Find volume of cylinder"""
        return math.pi * self.r ** 2 * self.h

    def area(self):
        """Finds area od cylinder"""
        return 2 * math.pi * self.r ** 2 + 2 * math.pi * self.r * self.h


class Cuboid(Shape3D):
    """Calls on Shape3D to print the area & volume
    or return an invalid argument"""
    def __init__(self, w: int, l: int, h: int):
        self.w = w
        self.l = l
        self.h = h

    def volume(self):
        """Finds volume of cuboid"""
        return self.w * self.l * self.h

    def area(self):
        """Finds area of cuboid"""
        return (2 * self.w * self.l) + (2 * self.w * self.h) + (2 * self.l * self.h)


class Cube(Cuboid):
    """Calls on cuboid to find the volume and
    area of the cube"""
    def __init__(self, w: int):
        super().__init__(w, w, w)
