# 01
# very lnong method
# read a poem and find it contains "twinkle"
checkString="twinkle"
# open a file
filePoems=open("/laboratory/python/python learning/resources/poems.txt","r")
# assign read variable
filePoemsRead=filePoems.read()
print(filePoemsRead.count(checkString)) #returns occurence of the charcter
print(filePoemsRead.find(checkString)) #returns starting position of the charcter
filePoems.close()
# short method
newMethodFile=open("/laboratory/python/python learning/resources/poems.txt","r") #open file
newMethodFileRead=newMethodFile.read() #read file
if checkString in newMethodFileRead:
    print("strings in the file")
else:
    print("strings not in the file")
newMethodFile.close() 
