'''
Super Simple Functions!
A script that illustrates functions and function calls in Python
Melissa Holmes, Fall 2026
'''

#function definitions
def fun_paramsReturn(x, y):
    return x + y

def fun_paramsNoReturn(x, y):
    print(x + y)

def fun_noParamsNoReturn():
    print("No parameters were passed to this function")

def fun_noParamsReturn():
    #this function randomly returns 67
    return 67


# main part of program

print("Calling fun_paramsReturn")

sum = fun_paramsReturn(3, 4)  #assigns return value to a variable
print("Sum = " + str(sum))

print(fun_paramsReturn(5, 10))   # uses the function call as a parameter

print()
print("Calling fun_paramsNoReturn")

fun_paramsNoReturn(7, 8)

#the line below is for testing.  It returns "None" because the function does not
#return a value that can be used as the parameter
print(fun_paramsNoReturn(7, 8))

print()
print("Calling fun_noParamsNoReturn")

fun_noParamsNoReturn()

print()
print("Calling fun_noParamsReturn")

weirdVar = fun_noParamsReturn()
print(weirdVar)

