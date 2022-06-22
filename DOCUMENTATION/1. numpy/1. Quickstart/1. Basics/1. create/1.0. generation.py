'''
Often, the elements of an array are originally unknown, but its size is known. 
    Hence, NumPy offers several functions to create arrays with initial 
    placeholder content.
        These minimize the necessity of growing arrays, an expensive operation.
'''
'''
--> The function zeros creates an array full of zeros, 
--> the function ones creates an array full of ones, 
--> and the function empty creates an array whose initial content is random 
    and depends on the state of the memory. 
    
--> By default, the dtype of the created array is float64, 
    but it can be specified via the key word argument dtype.
'''
import numpy as np

# create array
# one dimensional array
print("one dimensional array:")

# fetch numbders from a range
# range is 10, total numbers in range
# numbers from 0 to 9 will be placed in array, sorted.
arrayRangeOneDimensional=np.arange(10)
print(f"array with Range in One Dimensional:\n{arrayRangeOneDimensional}")

# create sequences
# sequence with pre-defined difference
'''
arrayName=np.arange(lower limit number, upper limit number + 1, sequence difference)
''' 
# lower limit=1, upper limit = 9, difference = 2
# 1,3,5,7,9
arraySequenceDifference=np.arange(1,10,2)
print(f"array Sequence Difference:\n{arraySequenceDifference}")
# sequence with pre-defined elements
'''
arrayName=np.linspace(lower limit number, upper limit number, total elements)
''' 
# lower limit=1, upper limit = 10, elements = 
# 1,3.25,...,7.75,10
arraySequenceQuantity=np.linspace(1,10,5)
print(f"array Sequence Quantity:\n{arraySequenceQuantity}")
...

# two dimensional array
print("two dimensional array:")

# create array with all elements as zero, 2 rows and 3 columns
# function used is ---> zeros
zeroArray=np.zeros((5,8))
print(f"all elements are zero in Array:\n {zeroArray}")

# create array with all elements as one, 3 rows and 4 columns
# function used is ---> ones
oneArray=np.ones((5,8))
print(f"all elements are one in Array:\n {oneArray}")

# create array with random elements , 2 rows and 3 columns
'''
function empty:
    a.  creates an array 
    b.  whose initial content is random,
        b.a. depends on the state of the memory
'''
# function used is ---> ones
oneArray=np.empty((2,3))
print(f"random elements in Array:\n {oneArray}")

# fetch numbders from a range
# shape in matrix
# range is 10, total numbers in range
# numbers from 0 to 9 will be placed in array, sorted.
# rows = 2, columns = 5
arrayRangeTwoDimensional=np.arange(10).reshape(2,5)
print(f"array with Range in Two Dimensional:\n{arrayRangeTwoDimensional}")