'''
sets: collection of non-repetitive elements. object data type
1. no repetition allowed
2. dataypes containing unique values
3. unordered.
4. un-indexed, i.e. elements doens't have a position, can't be accessed by position number
5. immutable, i.e. can't be changed.
6. cannot contain duplicate values.
7. items can be added to a set. new items are added at the end.
8. datatypes that can be added are: characters, integers, 
9. datatypes that can't be aded are: lists, .they are unhashable.
10. elements can tbe removed from the set


hashable: An object is hashable if it has a hash value that does not change during its entire lifetime.
'''

# empty dictionary
import msilib
from tkinter import Variable


empty_dictionary={}
print(type(empty_dictionary))

# create empty set
empty_set=set()
print(type(empty_set))

# Set
mySet={1,"name",1, 874, 510}


# print all unique values in a set --> first unique value is returned
# other repetitive value are ignored
print(mySet)

# oerations on set
# length of a set --> only unique value are considered
print(len(mySet))
# remove element from a set 
# set.remove() --> only if present
print(mySet.remove(874)) #if elmeent available
# print(mySet.remove(5)) #if element is not available. --> returns error
# set.pop() --> removes arbitray elment from set and returns the same element
print("set.pop", mySet.pop()) 
# set.clear --> emprties the set
print("set.clear", mySet.clear())
# set.union({}) --> returns a set with elments from both sets
print("set.union", mySet.union({23,5,6,"name"}))
# set.intersection //returns comon elments from both sets.
print("set.intersection", mySet.intersection({1,5,6}))

# operation on two sets
set1={1,5,'name',9}
set2={5,'love',9}
# union of two sets
print('union of two sets', set1.union(set2))
# intersection of two sets
print('intersection of two sets', set1.intersection(set2))


# adding elements to a set
mySet.add(5) #adding integers
print(mySet)
mySet.add("hyper") #adding strings
print(mySet)
# mySet.add(1,5) #adding multiple integers --> mutliple integers can't be added
# print(mySet)
print(mySet.add(74)) #printing sets and adding at the same time
# mySet.add([1,5,"jolly"]) #adding lists -->lists can't be added to a set
# mySet.add({1:2,5:8}) #adding dictionary -->dictionary can't be added to a set
# mySet.add({1,2}) #adding sets -->sets can't be added to set
mySet.add((1,5,8)) #adding tuples
print(mySet)








