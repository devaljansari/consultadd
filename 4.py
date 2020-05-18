
'''Write a Python program which accepts the radius of a circle 
from the user and compute the area.'''

print("Method 1 is: ")
print()
r = float(input("Enter the radius: "))
A = 3.14 *(r**2)
print("Area of a circle is: ",A)
print()
print()


print("Method 2 is: ")
print()
from math import pi
area = pi*(r**2)
print("Area of a circle is: ",A)