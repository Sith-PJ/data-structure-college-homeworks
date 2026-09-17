"""
Write a Python program that accepts an integer (n) and print a 3-tier Christmas tree 
with a star at the top.
"""

n = input('Please enter a number: ')
print('   *')
print(' ', n * 3)
print('', n * 5)
print(n * 7)
print('  ', n)