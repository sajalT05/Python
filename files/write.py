'''
<_io.TextIOWrapper name='/laboratory/python/python learning/resources/write.txt' mode='w' encoding='cp1252'>
// chill, not error
'''

'''
// a new file is created if not present.
'''

'''
// open the file in writre mode.
// use write() to write to the file.
// -> overwrites the whole file.
// use close() to close the file which has been opened. --> very important
// integers or floats have to be converted into string befre writing them into the file.

// can be called multiple times.
'''

# // write a file
# open file
# disk is the default home folder home
# to avoid error in opening file, use address of file while opening
# assign file opening variable to FileVariable
FileVariable=open("/laboratory/python/python learning/resources/write.txt","w") # use w for write mode
# write the file
# use write()
# place string inside write() that has to be writeen in file
# no varibale need to be assigned
FileVariable.write("This is the new written line.")
# print file text during writing doesn't works 
print(FileVariable) #print FileVariableWrite --> no return
# close the file
FileVariable.close() # --> very important

# print the new written file
# assign file opening variable to FileVariable
FileVariableNew=open("/laboratory/python/python learning/resources/write.txt")
print(FileVariableNew.read())
FileVariableNew.close()
