"""
• Write a program that asks user for a number and checks whether or not it is a 
palindrome number. 
• A palindrome is a word, number, phrase, or other sequence of symbols that reads the 
same backwards as forwards, such as 14741, madam, racecar.
"""

number = input("Please enter a number: ")
if number != number[::-1]:
    print(f"{number} is NOT a palindrome.")
else:
    print(f"{number} is a palindrome.")