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
# manual array shape = 2X3
# [1,5,9],[10,50,90]
arrayTwoDimensionManual=np.array(([1,5,9],[10,50,90]))
# create array sequence
# required sequence shape = 3X2
# [0,1],[2,3],[4,5]
arrayTwoDimensionSequence=np.arange(6).reshape(3,2)

# array multiplication
# matrix multiplication
# @ operator
# one dimention matrices
# array1(1,3) X array2(1,3) = array(,2)
arrayOneDimensionMultiplication=arrayOneDimensionManual@arrayOneDimensionSequence
print(f"array One Dimension Multiplication: \n {arrayOneDimensionMultiplication}")
# two dimention matrices
# array1(2,3) X array2(3,2) = array(2,2)
arrayTwoDimensionMultiplication=arrayTwoDimensionManual@arrayTwoDimensionSequence
print(f"array Two Dimension Multiplication: \n {arrayTwoDimensionMultiplication}")