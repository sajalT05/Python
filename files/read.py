'''
<_io.TextIOWrapper name='/laboratory/python/python learning/resources/write.txt' mode='w' encoding='cp1252'>

// check file path used.
// check another read() like command is used or not. 
'''

'''
// open the file in read mode.
// use read() to read the file.
// -> just read the file.
// use close() to close the file which has been opened. --> very important
'''

'''
// read() can be called only one time
// readline() can be called multple time.
// if read() is used, readline() returns blank.
'''

# importing os module
import os

# check path of file
print("File address:", os.path.abspath("sample.txt"))

# print files and foldes name in 'resources' folder
for resourcesList in os.listdir("/laboratory/python/python learning/resources/"):
	print(resourcesList)


# // Read whole text of a file
# open file
# disk is the default home folder home
# to avoid error in opening file, use address of file while opening
# assign file opening variable to FileVariable
FileVariable=open("/laboratory/python/python learning/resources/sample.txt","r") # read mode is default
# read contents of file
# assign read file variable to readFileVariable
readFileVariableText=FileVariable.read() #read all characters in file
readFileVariableText10=FileVariable.read(10) #read first 10 characters in file
readFileVariableLines=FileVariable.readline() #read first 3 lines
# print contents of file 
print("Print all characters in file: \n", readFileVariableText) #print whole text
'''
// when read() is used.
// a new variable returns empty for reading characters in the file in a single file operation. e.g.read(5)
'''
print("Print first 10 characters in file: \n", readFileVariableText10) #print whole text
'''
// if a read() is used before readline(), then readline() returns no value
// close the current file and open again to print lines separately.
// this may occue while reading and modifying files at the same time, also.
'''
print("Read lines in file, when read() function is used : ", readFileVariableLines) #print readFileVariable5
# close file
FileVariable.close()

# //Read lines in a file
FileVariable1=open("/laboratory/python/python learning/resources/sample.txt","r") # read mode is default
print("Printing lines: ")
# print first line
FileVariable1Lines=FileVariable1.readline()
print("Print Line1: \n", FileVariable1Lines)
# print second line
FileVariable1Lines=FileVariable1.readline()
print("Print Line2: \n", FileVariable1Lines)
# print third line
FileVariable1Lines=FileVariable1.readline()
print("Print Line3: \n", FileVariable1Lines)
FileVariable1.close()