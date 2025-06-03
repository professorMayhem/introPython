########################################################
#
#    Melissa Holmes    Introductory Python classes
#    Example of a function to error-check for int input
#
########################################################

doAgain = True
while doAgain:
    try:    #put the code that might break in the try clause
        user_input = input("Enter an integer: ")
        num = int(user_input) #will break if user does not enter an int
        
        print("Input is valid:  ", num)
        doAgain = False  # exit the loop if input is valid
    except ValueError:
        # except clause is executed if the input is not a valid integer
        print("Invalid input. Please enter an integer.")
