"""
Write a program that asks for begin and end and prints only even numbers between 
them (exclusive).
"""

begin = int(input("Begin: "))
end = int(input("End: "))
i = begin
numbers = []

while i <= end:
    if i % 2 == 0 and i != begin and i != end:
        numbers.append(str(i))
    i += 1
print(" ".join(numbers))