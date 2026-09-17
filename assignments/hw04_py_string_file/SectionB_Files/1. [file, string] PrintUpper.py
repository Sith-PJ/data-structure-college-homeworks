"""Write a program to read a file and print the first five lines all in upper case.

Source: https://www.w3resource.com/python-exercises/file/index.php
"""

def first_five_lines_upper(file_name):
    save_line = ""
    with open(file_name, 'r') as f:
        for i, line in enumerate(f):
            if i >= 5:
                break
            save_line += line.upper()
    return save_line

def main():
    file_name = input("Filename: ")
    print(first_five_lines_upper(file_name))

if __name__ == "__main__":
    main()