
#set up empty list
wordList = []

#loop through the file and copy words into a wordList
f = open("words_alpha.txt", "r")

for x in f:
  wordList.append(x.strip())

#close the file
f.close()
