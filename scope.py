##########################################
#
#   Exploring Scope in Python
#   Download and modify the code to experiement with scope
#
##########################################

# global variables are created outside of any functions
# global variables are visible in all the functions


global_var = "global!"

def myFunFunction():
    # a and b, below, are local variables
    # these instances of a and b are only visible in this function
    a = "Hello World"
    b = 3
    print("From myFunFunction: " + global_var)


def anotherFunction(X, Y):
    # X is only visible in this function
    print("X = " + str(X) + " and Y = " + str(Y))

    #change X and Y
    X = 0
    Y = 2
    print("X = " + str(X) + " and Y = " + str(Y))

    
def loopFun(theList, N):
    for i in range(N):
        theList[i] += 1

    # in Python, i and loopvar are visible outside the block
    # not true with all languages
    print("i = " + str(i))
    
def main():
    
    a = 42
    b = 43
    mainList = [2, 4, 6, 8, 3, 5, 7]

    # print the variables that are local to main
    # instances of a and b are different than those defined in myFunFunction
    print("Printing a and b from main:")
    print(a)
    print(b)
    print()


    # function calls in main
    print("Calling myFunFunction from main")
    myFunFunction()
    print("Calling anotherFunction from main")
    anotherFunction(a, b)
    print()

    # lists are pass by reference
    # print the list, then call the function that changes the list,
    # then print again
    print("Doing the list stuff")
    print(mainList)
    loopFun(mainList,5)
    print("after the function call")
    print(mainList)


if __name__ == '__main__':
    main()
