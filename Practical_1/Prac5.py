# Program to solve quadratic equation

import math
print("A quadratic equation is the format of a*x^2+b*x+c=0")
a=int(input("a= "))
b=int(input("b= "))
c=int(input("c= "))
d=(math.pow(b,2)-(4*a*c))
if(d<0):
    print("Roots are imaginary")
    exit()
b*=-1
root1=(b-d)/(2*a)
root2=(b+d)/(2*a)
print("root1 & root2 are",root1,root2)    