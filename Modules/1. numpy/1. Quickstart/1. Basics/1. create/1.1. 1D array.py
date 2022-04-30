'''
Sequence

One Dimensional array:
1. contains only one list.
2. can contain any number of elements in list.

[]

'''
import numpy as np
# create array
# One Dimensional array
# Manual Creation
oneDimensionalArray=np.array(([5,6,3]))
print("One Dimensional array:")
print(oneDimensionalArray)

print("\n")

# Automatic/Random Generation
print("Automatic/Random Generation:")
# take numbers from a range (sorted)
oneDimensionalArrayRandom=np.arange(5,10)
# lower value is included but higher value is not included
print("One Dimensional Array, random numbers in range, 5 to 9:")
print(oneDimensionalArrayRandom)