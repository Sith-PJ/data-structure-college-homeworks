"""
Write a program that asks user for a number and prints each digit in the reverse order.

Source: https://pynative.com/python-basic-exercise-for-beginners/
"""

number = input("Enter a number: ")
print("Digits in reverse: " + " ".join(number[::-1]))