import numpy as np
# one dimenional array
# create array manually
# [1,5,9]
arrayOneDimensionManual=np.array([1,5,9])
# two dimenional array
# create array manually
# [1,5,9],[10,50,90]
arrayTwoDimensionManual=np.array(([1,5,9],[10,50,100]))

# exponent

# b square 2 = b^2 = b**2

# exponent of one dimensional arrays
# [1,5,9]**2 = [1,25,81]
print(f"exponent of 1D array(2):\n {arrayOneDimensionManual**2}")

# exponent of two dimensional arrays
# [1,5,9],[10,50,100]**2 = [1,25,81],[100,2500,10000]
print(f"exponent of 2D array(2):\n {arrayTwoDimensionManual**2}")

