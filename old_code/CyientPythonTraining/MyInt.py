import functools
@functools.total_ordering 

class MyInt:
    def __init__(self,v):
        self.value = v

    def __add__(self, other):
        z = self.value + other.value
        return MyInt(z)

    def __sub__(self, other):
        z = self.value - other.value
        return MyInt(z)

    def __eq__(self, other):
        return self.value == other.value
    
    def __gt__(self, other):
        return self.value > other.value


    def __str__(self):
        return "MyInt(%d)" %(self.value,)

class Fraction:

    def __init__(self,num,den):
        self.num = num
        self.den = den

    def __str__(self):
        return "Fraction(%d, %d)" %(self.num, self.den)

    def __add__(self, other):
        num = (self.num * other.den) + (self.den * other.num)
        den = self.den * other.den 
        return Fraction(num, den)
    

class Poly:

    def __init__(self, *args):
        self.poly = args

    def __str__(self):
        return "Poly(%d )" %(self.poly)

    
        
        
