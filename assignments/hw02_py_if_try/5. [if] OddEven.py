"""
Write a program that determines whether a given number (accepted from the user) is 
even or odd and prints an appropriate message to the user.

Source: https://www.w3resource.com/python-exercises/python-basic-exercise-21.php
"""

number = int(input("Enter a number: "))

if number % 2 == 0:
    print(number, "is an even number")
else:
    print(number, "is an odd number")