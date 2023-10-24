# -*- coding: utf-8 -*-
"""
Write a Python program which accepts the radius of a circle from the user and compute the area.
"""

import math #importing math method from the library to get the value of pi

radius = int(input("Enter the radius: ")) #getting the radius value from the user

area = math.pi * (radius ** 2) #selecting the value of pi form the math library

print("The area of the circle: ",area) #printing the result
