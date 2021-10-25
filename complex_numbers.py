#!/usr/bin/env python

import math

class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    
    def __str__(self):
        ret = ""
        real_str = "%.2f" % self.real
        imag_str = "%.2f" % self.imag
        if self.real > 0 or self.real < 0:
            ret += real_str
        if self.imag > 0 or self.imag < 0:
            if self.imag > 0:
                if ret != "":
                    ret += " + " + imag_str + "i"
                else:
                    ret += imag_str + "i"
            else:
                if ret != "":
                    new_imag = -1 * self.imag
                    imag_str = "%.2f" % new_imag
                    ret += " - " + imag_str + "i"
                else:
                    ret += imag_str + "i"
        if ret == "":
            ret += real_str
        return ret
    
    def __add__(self, other):       
        new_real = self.real + other.real
        new_imag = self.imag + other.imag
        new_complex = Complex(new_real,new_imag)
        return str(new_complex)
    def __sub__(self, other):
        new_real = self.real - other.real
        new_imag = self.imag - other.imag
        new_complex = Complex(new_real,new_imag)
        return str(new_complex)
    def __mul__(self, other):
        new_real = (self.real * other.real) - (self.imag * other.imag)
        new_imag = (self.real * other.imag) + (self.imag * other.real)
        new_complex = Complex(new_real,new_imag)
        return str(new_complex)
    def __div__(self, other):
        divisor = (other.real ** 2) + (other.imag ** 2)
        new_real = ((self.real * other.real) + (self.imag * other.imag)) / divisor
        new_imag = ((self.imag * other.real) - (self.real * other.imag)) / divisor
        new_complex = Complex(new_real,new_imag)
        return str(new_complex)
    def mod(self):
        new_real = math.sqrt(self.real ** 2 + self.imag ** 2)
        new_complex = Complex(new_real, 0.0)
        return str(new_complex)

a = [float(x) for x in raw_input().split(' ')]
b = [float(x) for x in raw_input().split(' ')]
ca = Complex(a[0],a[1])
cb = Complex(b[0],b[1])
print ca + cb
print ca - cb 
print ca * cb
print ca / cb
print ca.mod()
print cb.mod()

