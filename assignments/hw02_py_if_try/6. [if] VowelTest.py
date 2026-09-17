"""
Write a program to test whether a given letter is a vowel or not.

Source: https://www.w3resource.com/python-exercises/python-basic-exercise-24.php 
"""

vowel = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
letter = input("Enter a letter: ")

if len(letter) == 1 and letter.isalpha():
    if letter in vowel:
        print(f"'{letter}' is a vowel")
    else:
        print(f"'{letter}' is NOT a vowel")
