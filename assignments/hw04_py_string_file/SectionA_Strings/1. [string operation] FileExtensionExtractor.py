"""Write a Python program that accepts a filename from the user and prints the extension 
of the file. 

Source: https://www.w3resource.com/python-exercises/python-basic-exercise-7.php
"""

filename = input("Input the Filename: ")
extension = filename.split(".")[1]
print(f"The extension of the file: {extension}")