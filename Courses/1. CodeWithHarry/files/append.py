'''
<_io.TextIOWrapper name='/laboratory/python/python learning/resources/append.txt' mode='a' encoding='cp1252'>

'''

'''
'''

'''
// open the file in append mode.
// use write() to apoend the file.
// -> a new file is created if not present.
// use close() to close the file which has been opened. --> very important.
// a new line is added, everytime the write() is used during append mode.

// can be called multiple times.
'''

# // append a file
# open file
# disk is the default home folder home
# to avoid error in opening file, use address of file while opening
# assign file opening variable to FileVariable
FileVariable=open("/laboratory/python/python learning/resources/append.txt","a") # use a for append mode
# write the file
# use write()
# place string inside write() that has to be appended in file
# no varibale need to be assigned
FileVariable.write("This is the new appended line.")
# print file text during appedning doesn't works 
print(FileVariable) #print FileVariableWrite --> no return
# close the file
FileVariable.close() # --> very important

# print the new appended file
# assign file opening variable to FileVariable
FileVariableNew=open("/laboratory/python/python learning/resources/append.txt")
print(FileVariableNew.read())
FileVariableNew.close()