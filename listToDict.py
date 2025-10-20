


# get sides from user
# store them in a list

theList = []

n = int(input("How many sides?"))

for i in range(n):
    theList.append(input("Enter the side label:  "))

print("The list = " + str(theList))

# Create the dictionary of toss counts
# use the sides as keys and set values to 0

theDict = dict.fromkeys(theList, 0)

print("The dictionary = " + str(theDict))

# toss the die - choose a side randomly, increase count value

# get side from user
side = input("Enter the side: ")
if side in theDict:
    theDict[side] += 1

print("The dictionary = " + str(theDict))    
# research ways to count things using a dictionary
