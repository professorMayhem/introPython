########################################################
#
#    Melissa Holmes    Introductory Python classes
#    Example of a function to error-check for int input
#
########################################################


def checkInput():
    while True:
        try:    #put the code that might break in the try clause
            user_input = int(input("Enter an integer: "))
            num = int(user_input) #throws ValueError if user does not enter int
            
            print("Input is valid:  ", num)
            return num            #return the valid number
        
        except ValueError:
            # except clause is executed if the input is not a valid integer
            print("Invalid input. Please enter an integer.")
    


# function call
checkedNum = checkInput()


