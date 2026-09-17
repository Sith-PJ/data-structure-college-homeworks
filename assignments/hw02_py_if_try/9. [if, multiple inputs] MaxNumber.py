"""
Given three numbers, find the largest among them.
"""

numbers = list(map(int, input("Please enter three numbers: ").split()))
largest_number = max(numbers)
print("Largest number:", largest_number)