"""
Write a program to prompt the user for hours and rate per hour to compute gross pay.
Source: 
• https://www.py4e.com/lectures3/Pythonlearn-02-Expressions.pptx
"""

hours = input("Enter Hours: ")
rate = input("Enter Rate: ")
pay = float(hours) * float(rate)
print("Pay:", pay)