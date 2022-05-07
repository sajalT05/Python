'''
Sequence of Sequences

Two Dimensional array:
1. contains rows and columns
2. rows is the horizontal layer.
    a. rows are number of lists.
3. column is the vertical layer.
    a. columns are number of elements in lists.
    b. length of lists.

[],[]

'''
import numpy as np
# create array
# Two Dimensional array
# Manual Creation
# number of lists will be rows and number of elements will be column
twoDimensionalArray=np.array(([5,6,3],[6,8,9]))
print("Two Dimensional array:")
print(twoDimensionalArray)

print("\n")

# Automatic/Random Generation
print("Automatic/Random Generation:")
# take numbers from a range (sorted)
'''
array=np.arange(|range of numbers|).reshape(rows,columns)

array   --> array to be created
np      --> imported numpy module abreviation
arange  --> use numbers in the defined range.
        --> 0 is the default
        --> lower limit is included
        --> upper limit is excluded
reshape --> define number of rows and column
rows    --> number of lists
columns --> number of elements in a single list
.....
//product of rows and columns is equal to range of numbers.
numbers in range = rows*columns
'''
# range = 2 to 13
# total numbers = 12
# rows = 3 & columns = 4 
twoDimensionalArrayRandom=np.arange(2,14).reshape(3,4)
# lower value is included but higher value is not included
print("Two Dimensional Array, random numbers in range, 2 to 13:")
print(twoDimensionalArrayRandom)