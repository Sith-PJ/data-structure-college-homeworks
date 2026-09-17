"""
Write a program that determines whether a given year (in A.D.) is a leap year. 
• Leap year is a year that has 366 days. 
• How to determine whether a year is a leap year 
    •   Any year that is divisible by 4 is a leap year 
    • Except when it is divisible by 100, in which case it is not a leap year 
    • Except when it is divisible by 400, in which case it is a leap year
"""

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

year = int(input("Please enter a year in A.D.: "))
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is NOT a leap year.")
    

