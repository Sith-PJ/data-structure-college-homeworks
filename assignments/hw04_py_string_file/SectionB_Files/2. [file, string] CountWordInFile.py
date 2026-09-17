"""Write a program to count the frequency of a given word in a file. 

Source: https://www.w3resource.com/python-exercises/file/index.php
"""

def count_word_in_file(file_name, word):
    count = 0
    with open(file_name, 'r') as f:
        for line in f:
            if word in line:
                count += 1
    return count

def main():
    file_name = input("Filename: ")
    word = input("Word to count: ")
    print(count_word_in_file(file_name, word))

if __name__ == "__main__":
    main()
