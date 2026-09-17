"""Check if a user-entered string contains any digits

Source: https://pynative.com/python-basic-exercise-for-beginners/
"""

def CheckDigit(word):
    count = 0
    for i in range(len(word)):
        if word[i].isdigit():
            count += 1
    return count

def main():
    word = input("Enter a string: ")
    if CheckDigit(word) == 0:
        print("The string does not contain any digits.")
    elif CheckDigit(word) > 0:
        print("The string contains at least one digit.")

if __name__ == "__main__":
    main()