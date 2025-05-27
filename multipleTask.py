#####################################################
#
#   Melissa Holmes              Summer 2025
#
#   Example of a program that has multiple parts
#   and how to documented it, and print narrative
#
#####################################################

# Task 1:  print Hello World
print("Task 1:  Print Hello World")
print("Hello World!")

#Task 2:  Get name, print Hello Name
print()   #prints a blank line
print("Task 1:  Print Hello Name")
name = input("What is your name?  ")
print("Hello " + name)

#Task #3:  Do some math
print()
print("Task 3:  doing some math")
x = int(input("Enter the length  "))
area = x * x
print("The area of a square with side length " + str(x) + " is " + str(area))
# note the use of the str function in the code above
# this is needed to convert numbers to strings for concatenation
