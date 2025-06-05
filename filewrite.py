
# set up a list for illustrative purposes

myList = ["hello", "world", "how", "are", "you?"]

# use the "w" option to create new file if it does not exist
# if the file does exist, "w" will overwrite the contents

with open("myfile.txt", "w") as f:
    f.write("This is the file:\n")

    #loop through the list to write each item
    for x in myList:
        f.write(x + " ")



