#!/usr/bin/env python

import math


#Area, diameter and perimeter of a CIRCLE
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        area = math.pi*(self.radius**2)
        return area

    def diameter(self):
        diameter = 2*self.radius
        return diameter

    def perimeter(self):
        perimeter = 2*math.pi*self.radius
        return perimeter


#class for area and perimeter of a RECTANGLE
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        area = self.length * self.width
        return area

    def perimeter(self):
        perimeter = 2 * (self.length + self.width)
        return perimeter


if __name__ == '__main__':
    c = Circle(3)
    a = c.area()
    d = c.diameter()
    p = c.perimeter()

    r = Rectangle(2,3)
    ar = r.area()
    pe = r.perimeter()

    print a
    print d
    print p

    print "\n", ar
    print pe