"""
Write a program to test whether a number is within 100 of 1000 or 2000.

Source: https://www.w3resource.com/python-exercises/python-basic-exercise-17.php
"""

def isInRange(number):
    return 900 <= number <= 1100 or 1900 <= number <= 2100

number = int(input("Enter a number: "))
print(isInRange(number))