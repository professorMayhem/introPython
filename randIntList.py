#############################################

#    Melissa Holmes
#    Python code example for Module 3 Quiz

#############################################

import random

def makeRandIntList(size):

    randList = []

    for i in range(size):
        randList.append(random.randint(1, 100))

    return randList


myRandList = makeRandIntList(25)

print(myRandList)

