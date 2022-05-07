import numpy as np
# create an array with 15 numbers, from 0 to 14
# rows=5,colums=3
# arange method: used to arrange numbers in a range, in an arrays.
# reshape method: used to shape numbers in rows & columns, in an arrays.
numberArray=np.arange(15).reshape(5,3)
#print array
print(f"print array: {numberArray}\n")
# shape of array
print(f"shape of array: {numberArray.shape}\n")
# dimensions in array
print(f"dimensions in array: {numberArray.ndim}\n")
# size of array
print(f"size of array: {numberArray.size}\n")
# data type of array
print(f"data type of array: {numberArray.dtype}\n")
# item size of array
print(f"item size of array: {numberArray.itemsize}\n")

