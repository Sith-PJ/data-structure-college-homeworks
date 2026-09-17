"""Write a function that takes a filename as input and returns the total number of 
characters in that file (including spaces and newlines).  Write a program to test the 
function. 

Source: https://pynative.com/python-file-handling-exercises/
"""

def count_char_in_file(file_name):
    with open(file_name, 'r') as f:
        num = len(f.read())
    return num

def main():
    file_name = input("Filename: ")
    print(f"Number of characters: {count_char_in_file(file_name)}")

if __name__ == "__main__":
    main()