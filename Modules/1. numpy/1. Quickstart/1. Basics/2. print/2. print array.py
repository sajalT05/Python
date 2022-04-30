'''
When you print an array, NumPy displays it in a similar way to nested lists, 
    but with the following layout:
        • the last axis is printed from left to right,
        • the second-to-last is printed from top to bottom,
        • the rest are also printed from top to bottom, 
            with each slice separated from the next by an empty line.

a. One-dimensional arrays are then printed as rows, 
b. bidimensionals as matrices and tridimensionals as lists of matrices.
'''

'''
>>> a = np.arange(6) # 1d array
>>> print(a)
[0 1 2 3 4 5]
>>>
>>> b = np.arange(12).reshape(4, 3) # 2d array
>>> print(b)
[[ 0 1 2]
[ 3 4 5]
[ 6 7 8]
[ 9 10 11]]
>>>
>>> c = np.arange(24).reshape(2, 3, 4) # 3d array
>>> print(c)
[[[ 0 1 2 3]
[ 4 5 6 7]
[ 8 9 10 11]]
[[12 13 14 15]
[16 17 18 19]
[20 21 22 23]]]
'''
import numpy as np

print("\n1d array")
a = np.arange(6) # 1d array
print(a)

print("\n2d array")
b = np.arange(12).reshape(4, 3) # 2d array
print(b)

print("\n3d array")
c = np.arange(24).reshape(2, 3, 4) # 3d array
print(c)