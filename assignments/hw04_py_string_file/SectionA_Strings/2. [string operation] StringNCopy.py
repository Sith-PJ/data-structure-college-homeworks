"""Write a program that returns a string that is n (non-negative integer) copies of a given 
string. 

Source: https://www.w3resource.com/python-exercises/python-basic-exercise-20.php
"""

def StringNCopy(str, n):
    return str * n

def main():
    try:
        str = input("Enter a string: ")
        n = int(input("Enter the number of copies: "))

        if n > 0:
            print(StringNCopy(str, n))
        else:
            print("Plese enter a non-negative integer")
            
    except ValueError:
        print("Plese enter only a number")

if __name__ == "__main__":
    main()
        