# split an array

def arraysplit(arr,n):
    leftarray=arr[:n]
    rightarray=arr[n:]
    return leftarray,rightarray

# call
arr=[1,2,3,4,5,6,7,8,9,10]
n=3
print(arraysplit(arr,n))