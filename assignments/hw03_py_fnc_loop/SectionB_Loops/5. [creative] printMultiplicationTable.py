"""
Print multiplication table from 1 to 5 

Source: https://pynative.com/python-basic-exercise-for-beginners/
"""

i = 1
while i <= 5:
    print(f"{i}: ", end="")
    for j in range(1, 13):
        print(i * j, end=" ")
    i += 1
    print()