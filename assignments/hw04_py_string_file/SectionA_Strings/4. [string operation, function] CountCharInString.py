"""Write a function named count which accepts a string and a letter as arguments and 
returns the number of occurrences of the letter within the string.  Write a program to 
test the function. 

Source: http://do1.dr-chuck.com/pythonlearn/EN_us/pythonlearn.pdf
"""

def CountCharInString(string, character):
    count = 0
    for i in string:
        if character == i:
            count += 1
    return count

def main():
    string = input("Enter a string: ")
    character = input("Enter a character: ")
    print(f"There are {CountCharInString(string, character)} {character}'s in {string}.")

if __name__ == "__main__":
    main()