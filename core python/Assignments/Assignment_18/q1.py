# 1. Create a class Complex Number with data members as real and imag and add
# following methods :
# a. Constructor
# b. Destructor
# c. Overload +,- operator

class Complexnumber:
    def __init__(self,real=0,imag=0):
        self.real=real
        self.imag=imag

    def __add__(self, other):
        return Complexnumber(
            self.real+other.real,
            self.imag+other.imag
        )    
    def __sub__(self, other):
        return Complexnumber(
            self.real-other.real,
            self.imag-other.imag
        )
    def display(self):
        print(self.real,"+",self.imag,"i")

c1=Complexnumber(10,5)        
c2=Complexnumber(4,3)     

print('first complex number:')
c1.display()

print('second complex number')
c2.display()

c3=c1+c2
print('addition:')
c3.display()

c4=c1-c2
print('substraction')
c4.display()