"""
Write a program which repeatedly reads integers until the user enters “done”. Once 
“done” is entered, print out the total, count, and average of the integers. If the user 
enters anything other than an integer, detect their mistake using try and except and 
print an error message and skip to the next integers. 

Source: http://do1.dr-chuck.com/pythonlearn/EN_us/pythonlearn.pdf
"""

numbers = []

while True:
    try:
        number = input("Enter a number: ")
        if number == 'done':
            break
        
        number = int(number)
        numbers.append(number)

    except ValueError:
        print("Invalid input")

print("Total:", sum(numbers))
print("Count:", len(numbers))
print("Average:", sum(numbers) / len(numbers) if len(numbers) > 0 else 0)