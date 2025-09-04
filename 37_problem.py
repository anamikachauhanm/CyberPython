#write a program to calculate the hypotenuse of a right angled triangle using math module

import math
side1 = float(input("Enter the length of the perpendicular : "))
side2 = float(input("Enter the length of the base : "))
hypotenuse = math.sqrt(side1**2 + side2**2)
print(f"The length of the hypotenuse is: {hypotenuse:.2f}")  