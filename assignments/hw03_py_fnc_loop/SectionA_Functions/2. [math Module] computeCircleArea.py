"""
Write a program that calculates the area of a circle based on the radius entered by the 
user.

Source: https://www.w3resource.com/python-exercises/python-basic-exercise-4.php 
"""

import math

def circlearea(r):
    return math.pi * r ** 2

r = float(input("r = "))
print("Area =", circlearea(r))
