"""Write a while loop that starts at the last character in the string and works its way 
backwards to the first character in the string, printing each letter backwards. 

Source: http://do1.dr-chuck.com/pythonlearn/EN_us/pythonlearn.pdf 
"""

def StringBackward(str):
    string_reverse = []
    while len(str) > 0:
        string_reverse.append(str[-1])
        str = str[:-1]
    return ''.join(string_reverse)

def main():
    str = input("Please enter a string: ")
    print(f"Printed backward:     ", StringBackward(str))

if __name__ == "__main__":
    main()