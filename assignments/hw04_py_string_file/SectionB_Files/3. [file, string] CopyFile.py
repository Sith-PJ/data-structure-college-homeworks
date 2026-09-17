"""Write a program to copy the contents of a file to another file.

Source: https://www.w3resource.com/python-exercises/file/index.php
"""

def copy_file_contents(file_name, dest_file):
    with open(file_name, 'r') as f:
        data = f.read()
    with open(dest_file, 'w') as g:
        g.write(data)
        g.close()

def main():
    file_name = input("Copy from file: ")
    dest_file = input("copy to file:   ")

    copy_file_contents(file_name, dest_file)

if __name__ == "__main__":
    main()
