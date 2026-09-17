"""
Calculate income tax for the given income by adhering to the rules below 
Taxable Income  Rate (in %) 
First $10,000   0           
Next $10,000    10        
The remaining   20     

Source: https://pynative.com/python-basic-exercise-for-beginners/#h-exercise-12
calculate-income-tax
"""

income = int(input("Income: "))

if income <= 10000:
    print("Tax: None")
elif 10000 <= income <= 20000:
    tax = (income - 10000) * 0.1
    print("Tax:", tax)
elif income > 20000:
    tax = (income - 20000) * 0.2 + 1000
    print("Tax:", tax)
else:
    print("Invalid income")