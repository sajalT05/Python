'''
lists: containers to store value of any datatype
Lists can be chaged.
Mutable

'''


from operator import iadd


integerArray=[16,13,400,866,97,9]
print(integerArray) #print the input array

# list indexing
integerArray[2]=25 #replace value at third position with the new value
print(integerArray) #print updated array

# slicing a list
print(integerArray[1:3]) #print list from second position to fourth position
print(integerArray[::2]) #print array from beginning to end by skipping every second position character

# arranging list
# function executed changes the list's arrangemnet
# sorting list // list in ascending order // list.sort()
integerArray.sort()
print(integerArray)
# reverse list // list in descending order // list.reverse()
integerArray.reverse()
print(integerArray)
# append // adds a value at the end of the list // list.append() --> very important
integerArray.append(10)
print(integerArray)
#insert // adds a value at an index position // list.insert(1,"value")
integerArray.insert(1,457) # adds 457 at second index position
print(integerArray)
#remove // removes a value fromt the list // list.remove("value")
integerArray.remove(25)
print(integerArray)




