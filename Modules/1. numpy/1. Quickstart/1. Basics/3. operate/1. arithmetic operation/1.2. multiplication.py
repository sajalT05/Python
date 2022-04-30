'''
the product operator * operates elementwise in NumPy arrays
'''

import numpy as np
# one dimenional array
# create array manually
# [1,5,9]
arrayOneDimensionManual=np.array([1,5,9])
# create array sequence
# [0,1,2]
arrayOneDimensionSequence=np.arange(3)
# two dimenional array
# create array manually
# [1,5,9],[10,50,90]
arrayTwoDimensionManual=np.array(([1,5,9],[10,50,90]))
# create array sequence
# [0,1,2],[3,4,5]
arrayTwoDimensionSequence=np.arange(6).reshape(2,3)

# multiplication

# product of an integer with an array
# product with one dimensional array
# [1,5,9] * 2 = [2,10,18]
print(f"product of 1D array with integer(2):\n {arrayOneDimensionManual*2}")
# product with two dimensional array
# [1,5,9],[10,50,90] *2 = [2,10,18],[20,100,180]
print(f"product of 2D array with integer(2):\n {arrayTwoDimensionManual*2}")

# product of one dimensional arrays
# [1,5,9] * [0,1,2] = [0,5,18]
print(f"product of 1D arrays:\n {arrayOneDimensionManual*arrayOneDimensionSequence}")
# # difference of two dimensional array
# # [1,5,9],[10,50,90] - [0,1,2],[3,4,5] = [0,5,18],[30,200,450]
print(f"product of 2D array:\n {arrayTwoDimensionManual*arrayTwoDimensionSequence}")

