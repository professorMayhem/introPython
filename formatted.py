"""
Melissa Holmes
Program to illustrate how to get multiple inputs on one line
September, 2025
"""

#txt = "1 2 3"

txt = input("Enter three integers, separated by a space:   ")

myList = txt.split()   # splits on a space, converts txt to a list
print(myList)          # output list to check input

print(type(myList[0])) # checks the data type of the input

A = int(myList[0])     # get first value, convert to int, assign to A
B = int(myList[1])     # repeat with B, and then C
C = int(myList[2])

print(type(C))         # data type after casting

# use f-string to print the values of A, B and C
# note the formatting added to B
print(f"A = {A} and B = {B:.2f} and C = {C}.")

# just for fun, let's print the list on one line
for x in myList:
    #print(x)
    print(x, end=' ')  # use the end specifier to print on one line
