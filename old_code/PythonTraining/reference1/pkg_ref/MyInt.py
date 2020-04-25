import functools
@functools.total_ordering
class MyInt:
    def __init__(self,v):
        self.value = v
    def __add__(self, other):
        z = self.value + other.value 
        return MyInt(z)
    def __str__(self):
        return "MyInt(%d)" % (self.value,)
    def __sub__(self, other):
        z = self.value - other.value 
        return MyInt(z)
    def __eq__(self, other):
        return self.value == other.value 
    def __gt__(self, other):
        return self.value > other.value 
    def __call__(self,pow):
        z = self.value ** pow
        return MyInt(z)
        
        
###################
#from pkg.MyInt import Fraction 
#a = Fraction(1,2)
#b = Fraction(2,3)
#c = a + b 
#print(c) #Fraction(7,6)

class Fraction:
    def __init__(self,n,d):
        self.n = n 
        self.d = d
    def __add__(self, other):
        n = self.n * other.d + other.n * self.d
        d = self.d * other.d
        return Fraction(n,d)
    def __str__(self):
        return "Fraction(%d,%d)" % (self.n,self.d)

####################
px = Poly( 2, 1,1)   #an , an-1, ......,a0
qx = Poly( 3, 1,-1,2)
c = px + qx
print(c)  #Poly(3,3,0,3)


