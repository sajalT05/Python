'''
Sequence of Sequence of Sequences

Three Dimensional array:
>As in 2D array
1. contains rows and columns
2. rows is the horizontal layer.
    a. rows are number of lists.
3. column is the vertical layer.
    a. columns are number of elements in lists.
    b. length of lists.
>Additional
4. list of lists is the new axes.

[[],[],[]],[[],[],[]]

'''
import numpy as np
# create array
# Three Dimensional array
# Manual Creation
# number of lists will be ____
# in a ____, number of lists will be rows and number of elements will be column
threeDimensionalArray=np.array(([[5,6,3],[6,8,9]],[[5,7,9],[4,6,8]]))
print("Three Dimensional array:")
print(threeDimensionalArray)

print("\n")

# Automatic/Random Generation
print("Automatic/Random Generation:")
# take numbers from a range (sorted)
'''
array=np.arange(|range of numbers|).reshape(____,rows,columns)

array   --> array to be created
np      --> imported numpy module abreviation
arange  --> use numbers in the defined range.
        --> 0 is the default
        --> lower limit is included
        --> upper limit is excluded
reshape --> define number of rows and column
____   --> number of ____
rows    --> number of lists in a ____
columns --> number of elements in a single list
.....
//product of lists, rows and columns is equal to range of numbers.
numbers in range = ____*rows*columns
'''
# range = 5 to 28
# total numbers = 24
# ____ = 2
# rows = 3 & columns = 4
threeDimensionalArrayRandom=np.arange(5,29).reshape(2,3,4)
# lower value is included but higher value is not included
print("Three Dimensional Array, with 2 ____, random numbers in range, 5 to 28:")
print(threeDimensionalArrayRandom)