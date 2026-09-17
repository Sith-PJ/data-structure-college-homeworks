"""
Rewrite the following code fragment using try/except instead of if/else:
"""

x = int(input('x: '))
y = int(input('y: '))

try:
    result = x / y
    print(result)
except:
    print("Can't divide")