#!/usr/bin/env python

import math

class Complex(object):
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
        
    def __add__(self, no):
        real = self.real + no.real
        imag = self.imag + no.imag
        return Complex(real, imag)

        
    def __sub__(self, no):
        real = self.real - no.real
        imag = self.imag - no.imag
        return Complex(real, imag)
        
    def __mul__(self, no):
        real = self.real * no.real
        imag = self.imag * no.imag
        return Complex(real, imag)

    def __truediv__(self, no):
        real = self.real / no.real
        imag = self.imag / no.imag
        return Complex(real, imag)

    def mod(self):
        real = self.real % no.real
        imag = self.imag % no.imag
        return Complex(real, imag)

    def __str__(self):
        if self.imag == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imag >= 0:
                result = "0.00+%.2fi" % (self.imag)
            else:
                result = "0.00-%.2fi" % (abs(self.imag))
        elif self.imag > 0:
            result = "%.2f+%.2fi" % (self.real, self.imag)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imag))
        return result

if __name__ == '__main__':
     parts = input('').split(' ')
     output = Complex(float(parts[0]), float(parts[1]))
     print(output)
