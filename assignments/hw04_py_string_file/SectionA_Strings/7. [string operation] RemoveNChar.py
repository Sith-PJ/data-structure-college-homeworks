"""Write a program to remove first n characters from a string.

Source: https://pynative.com/python-basic-exercise-for-beginners/
"""

def RemoveNChars(word, remove_num):
    return word[remove_num:]

def main():
    try:
        word = input("Please enter a word: ")
        remove_num = int(input("Number of letters to remove: "))
        print(RemoveNChars(word, remove_num))

    except ValueError:
        print("Invalid input, Please enter a valid number.")

if __name__ == "__main__":
    main()