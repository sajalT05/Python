import numpy as np
# one dimenional array
# create array manually
# [1,5,9]
arrayOneDimensionManual=np.array([1,5,9])
# two dimenional array
# create array manually
# [1,5,9],[10,50,90]
arrayTwoDimensionManual=np.array(([1,5,9],[10,50,100]))

# boolean

# returns true or false, depending upon condition

# boolean with one dimensional arrays
# [1,5,9]>4 = [False,True,True]
print(f"boolean with 1D array(>4):\n {arrayOneDimensionManual>2}")

# boolean with two dimensional arrays
# [1,5,9],[10,50,100]>30 = [False,False,False],[False,True,True]
print(f"boolean with 2D array(30):\n {arrayTwoDimensionManual>30}")

