"""
Write a program to prompt the user for hours and rate per hour.  Create a function 
computepay() that takes hours and rate as input, computes and returns the gross pay.  
The function should give the employee 1.5 times the hourly rate for hours worked 
above 40 hours. 

Source: http://do1.dr-chuck.com/pythonlearn/EN_us/pythonlearn.pdf
"""

def computepay(hours, rate):
    if hours < 0 or rate < 0:
        return "Error: Invalid Hours or Rate."
    
    if hours > 40:
        over_time = hours - 40
        regular_pay = 40 * rate
        overtime_pay = over_time * (rate * 1.5)
        return int(regular_pay + overtime_pay)
    else:
        return int(hours * rate)

hours = int(input("Enter Hours: "))
rate = int(input("Enter Rate: "))

print("Pay =", computepay(hours, rate))
