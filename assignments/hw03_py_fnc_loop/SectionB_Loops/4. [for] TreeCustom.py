"""
Write a program that accepts an integer (n) and print a 3-tier Christmas tree with a star 
at the top.

"""

tiers = int(input("Number of tiers: "))
for i in range (1, tiers + 1):
    print(" " * (tiers - i) + f"{i}" * ((i * 2) - 1))
print(" " * (tiers - 2) + "|.|")