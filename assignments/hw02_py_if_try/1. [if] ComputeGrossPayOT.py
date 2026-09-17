"""
Write a program to prompt the user for hours and rate per hour to compute gross pay.  
Give the employee 1.5 times the hourly rate for hours worked above 40 hours.

Source: http://do1.dr-chuck.com/pythonlearn/EN_us/pythonlearn.pdf
"""

hours = int(input("Enter Hours: "))
rate = int(input("Enter Rate: "))

if 0 <= hours <= 40:
    pay = hours * rate
    print("Pay:", int(pay))
elif hours > 40:
    pay = (40 * rate) + ((hours - 40) * (rate * 1.5))
    print("Pay:", int(pay))
else:
    print("Error: Hours cannot be negative")
