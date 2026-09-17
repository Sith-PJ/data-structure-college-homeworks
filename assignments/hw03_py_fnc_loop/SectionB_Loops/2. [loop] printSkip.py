"""
Write a program that asks for x/y/z (for begin/end/step) and prints the numbers starting 
from x, stepping every z, and ending no more than y.
"""

begin = int(input("Begin: "))
end = int(input("End: "))
step = int(input("Step: "))
i = begin
numbers = []

while i < end:
    numbers.append(str(i))
    i += step

print(" ".join(numbers))