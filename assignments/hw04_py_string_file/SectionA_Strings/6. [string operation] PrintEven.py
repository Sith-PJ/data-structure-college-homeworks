"""Write a program to accept a string and display characters present at an even index 
number. 

Source: https://pynative.com/python-basic-exercise-for-beginners/ 
"""

def PrintEvenIndexChars(s):
    letter = []
    for i in range(len(s)):
        if i % 2 != 0:
            letter.append(s[i])
        else:
            letter.append(' ')
    return ''.join(letter)

def main():
    s = input("Please enter a word:       ")
    print(f"Letters at even positions: {PrintEvenIndexChars(s)}")

if __name__ == "__main__":
    main()
