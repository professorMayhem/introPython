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


def anotherFunction(X):
    # X is only visible in this function
    print("X = " + str(X))

def loopFun(N):
    for i in range(N):
        funvar = 0  # visible in loopFun
        print(i)

    # in Python, i and loopvar are visible outside the block
    # not true with all languages
    print(i)
    print(funvar)
    
def main():
    a = 42
    b = 43

    # print the variables that are local to main
    # instances of a and b are different than those defined in myFunFunction
    print(a)
    print(b)

    # function calls in main
    myFunFunction()
    anotherFunction(a)
    loopFun(5)


if __name__ == '__main__':
    main()
