#################################################################
#
#   Melissa Holmes
#
#   Code for Intro Python classes
#   While loop that runs as long as the user enters "y" or "yes"
#
#################################################################

repeat = True

while repeat:
    
    # do the repeating thing

    # the string method lower converts the input to all lowercase
    again = input("Would you like to repeat the thing?  Enter Y or Yes   ").lower()

    if again == "yes" or again == "y":
        repeat = True
    else:
        print("Goodbye!")
        repeat = False
    
