import array

array=array.array('i',[1,2,3])

print("array:", array)

# element wise
for i in array:
    print(i)

# index wise
for i in range(len(array)):
    print (array[i])