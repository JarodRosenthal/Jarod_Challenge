import math
class Complex:
    def __init__(self, a, b):
        self.a, self.b = a, b;
    def display(self):
        if self.a < 0.005 and self.a > -0.005:
            self.a = 0;
        if self.b < 0.005 and self.b > -0.005:
            self.b = 0;
        if self.a != 0:
            str1 = '%0.2f' % self.a;
            if self.b > 0:
                str1 += ' + %0.2fi' % self.b;
            elif self.b < 0:
                str1 += ' - %0.2fi' % -self.b;
        elif self.b != 0:
            str1 = '%0.2fi' % self.b;
        else:
            str1 = '0.00';
        print str1;
        
    def conjugate(self):
        return Complex(self.a, -self.b);
    def norm(self):
        return self.a*self.a + self.b*self.b;
    def scale(self, scalar):
        return Complex(self.a*scalar, self.b*scalar);

    
def add(a, b):
    return Complex(a.a + b.a, a.b + b.b);
def sub(a, b):
    return Complex(a.a - b.a, a.b - b.b);
def mul(a, b):
    return Complex(a.a * b.a - a.b * b.b, a.a * b.b + a.b * b.a);
def div(a, b):
    return mul(a, b.conjugate().scale(1.0/b.norm()));
    
x = Complex(0, 0);
y = Complex(0, 0);

[a, b] = raw_input().split();
x.a = float(a);
x.b = float(b);

[a, b] = raw_input().split();
y.a = float(a);
y.b = float(b);

add(x, y).display();
sub(x, y).display();
mul(x, y).display();
div(x, y).display();
print '%0.2f' % math.sqrt(x.norm());
print '%0.2f' % math.sqrt(y.norm());
