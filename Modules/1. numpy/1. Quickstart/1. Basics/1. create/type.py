'''
1. array() takes from 1 to 2 positional arguments
2. you can create an array from a regular Python list or tuple using 
    the array function.
3. The type of the resulting array is deduced from the type of the 
    elements in the sequences.
4. provide a single sequence as an argument.
5. array transforms:
        sequences of sequences into two-dimensional arrays, 
        sequences of sequences of sequences into three-dimensional arrays, 
        and so on.
'''

import numpy as np
# create array
# integer array
integerArray=np.array([1,5,9])
# print integer array
print(f"Integer array:\n {integerArray}")
# type of array
print(f"type of array: {type(integerArray)}")
# data type array
print(f"data type of array: {integerArray.dtype}")

print("\n")

# float array
floatArray=np.array([15.5,9.3,5.97])
# print float array
print(f"Float array:\n {floatArray}")
# type of array
print(f"type of array: {type(floatArray)}")
# data type of array
print(f"data type of array: {floatArray.dtype}")

print("\n")

# complex array
complexArray=np.array([15+5j,9+3j,5+9j])
# print complex array
print(f"Complex array: {complexArray}")
# type of array
print(f"type of array: {type(complexArray)}")
# data type of array
print(f"data type of array: {complexArray.dtype}")
# item size of array
print(f"data size of array: {complexArray.itemsize}")

print("\n")

# complex array type(2)
# creating complex array from integer elemnets array
# another argument is passed, dtype=complex
print("another argument is passed, dtype=complex")
complexArray2=np.array([15,9,5], dtype=complex)
# print complex array
print(f"Complex array(2): {complexArray2}")
# type of array
print(f"type of array: {type(complexArray2)}")
# data type of array
print(f"data type of array: {complexArray2.dtype}")
# item size of array
print(f"data size of array: {complexArray2.itemsize}")