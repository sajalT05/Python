'''

'''
# read a file
with open("/laboratory/python/python learning/resources/with_file.txt","r") as withFile:
    withFileRead=withFile.read() #Read file
print(withFileRead)
# write a file
# same variables can be used in with statements
with open("/laboratory/python/python learning/resources/with_file.txt","w") as withFile:
    withFileWrite=withFile.write("This is the changed written line.")
print(withFileWrite)
# append a file
# same variables can be used in with statements
with open("/laboratory/python/python learning/resources/with_file.txt","a") as withFile:
    withFileAppend=withFile.write("This is the new appended line.")
print(withFileAppend)
