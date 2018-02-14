#!/usr/bin/env python

import math


#class that adds real and imaginary parts of a Complex numbers
class Complex:
    def __init__(self, re = 0.0, im = 0.0):
        self.re = re
        self.im = im


    def __str__(self):
        if self.im >= 0:
            return "("+str(self.re)  +" + "+ str(self.im) + "i"+")"
        else:
            return "("+str(self.re)  +" - "+ str(abs(self.im)) + "i"+")"


if __name__  == '__main__':
    a = Complex(2,3)
    print a


