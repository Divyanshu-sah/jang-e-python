# User will input (2numbers).Write a program to swap the numbers

a = int(input('enter your 1st num :'))
b = int(input('enter your 2st num :'))

tamp = a
a = b
b = tamp
print(f"After swapping:\nFirst number: {a}\nSecond number: {b}")