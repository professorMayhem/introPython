###################################################################
#
#    Example Python code for intro Python classes
#    Dr. Melissa Holmes
#    Summer, 2025
#
###################################################################


# function to find the longest sequence of a value in a list

def longestSequence(coinflips, n, side):
    currentseq = 0
    maxseq = 0

    for i in range(n):
        if coinflips[i] == side:
            currentseq += 1
        else:            
            if currentseq > maxseq:
                maxseq = currentseq
            currentseq = 0
    return maxseq


def main():

    coinflips = [1, 0, 0, 0, 1, 1, 0, 1, 0, 0]
    n = len(coinflips)

    print("The longest sequence of Heads flips was " + str(longestSequence(coinflips, n, 0)))
    print("The longest sequence of Tails flips was " + str(longestSequence(coinflips, n, 1)))
    

    #example code below for creating empty list, passing to functions
    
    #call function to get n from user with exception handling
    # n = getNumFromUser()
    
    #create empty list
    # coinflips = []
    
    #call function to populate list, passing the list and n
    # populateList(coinflips, n)
