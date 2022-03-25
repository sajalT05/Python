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

# substraction

# difference of an integer with an array
# difference in one dimensional array
# [1,5,9] - 1 = [0,4,8]
print(f"difference of 1D array with integer(1):\n {arrayOneDimensionManual-1}")
# difference in two dimensional array
# [1,5,9],[10,50,90] - 1 = [0,4,8],[9,49,89]
print(f"difference of 2D array with integer(1):\n {arrayTwoDimensionManual-1}")

# difference of one dimensional array
# [1,5,9] - [0,1,2] = [1,4,7]
print(f"difference of 1D array:\n {arrayOneDimensionManual-arrayOneDimensionSequence}")
# difference of two dimensional array
# [1,5,9],[10,50,90] - [0,1,2],[3,4,5] = [1,4,7],[7,46,85]
print(f"difference of 2D array:\n {arrayTwoDimensionManual-arrayTwoDimensionSequence}")

