"""`
Write a function max3() to find the maximum of three numbers.  Write a program to 
test the function. 

Source: https://www.w3resource.com/python-exercises/python-functions
exercises.php 
"""

def max3(numbers):
    return max(numbers)

numbers = list(map(int, input("Enter three numbers: ").split()))
print("Max:", max3(numbers))