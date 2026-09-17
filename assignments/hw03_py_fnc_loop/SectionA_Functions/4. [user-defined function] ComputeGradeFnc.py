"""
Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, 
print an error message. If the score is between 0.0 and 1.0, print a grade using the 
following table: 
Score Grade 
>= 0.9 A 
>= 0.8 B 
>= 0.7 C 
>= 0.6 D 
< 0.6 F 
In grade computation, the program must create a function computegrade() that takes a 
score as its parameter and returns a grade as a string.

Source: http://do1.dr-chuck.com/pythonlearn/EN_us/pythonlearn.pdf
"""

def computegrade(score):
    if score < 0.0 or score > 1.0:
        return "Bad score"

    if score >= 0.9:
        return "A"
    elif score >= 0.8:
        return "B"
    elif score >= 0.7:
        return "C"
    elif score >= 0.6:
        return "D"
    else:
        return "F"

try:
    score = float(input("Enter Score: "))
    print(computegrade(score))
except:
    print("Bad score")