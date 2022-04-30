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

# addition of an integer with an array
# addition in one dimensional array
# [1,5,9] + 5 = [6,10,14]
print(f"sum of 1D array with integer(5):\n {arrayOneDimensionManual+5}")
# addition in two dimensional array
# [1,5,9],[10,50,90] + 5 = [6,10,14],[15,55,95]
print(f"sum of 2D array with integer(5):\n {arrayTwoDimensionManual+5}")

# addition

# addition of arrays
# sum of one dimensional array
# [1,5,9] + [0,1,2] = [1,6,11]
print(f"sum of 1D arrays:\n {arrayOneDimensionManual+arrayOneDimensionSequence}")
# sum of two dimensional array
# [1,5,9],[10,50,90] + [0,1,2],[3,4,5] = [1,6,11],[13,54,95]
print(f"sum of 2D arrays:\n {arrayTwoDimensionManual+arrayTwoDimensionSequence}")

