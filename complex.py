#!/usr/bin/env python

import math


#class that adds real and imaginary parts of a Complex numbers
class Complex:
    def __init__(self, re = 0.0, im = 0.0):
        self.re = re
        self.im = im
        self.number = self.re,  "+",self.im,"i"

    def __str__(self):
        return str(self.number)


if __name__  == '__main__':
    a = Complex(2)
    print a


