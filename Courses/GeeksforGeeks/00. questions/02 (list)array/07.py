# check monotonic nature of array

def arraynature(array):
    if(
        all(array[i] <= array[i+1] for i in range(len(array)-1)) or
        all(array[i] >= array[i+1] for i in range(len(array)-1))
    ):
        print("monotonic")
    else:
        print("not monotonic")

# test
arr1=[1,2,3,4,5,6,17,8,29,10]
arraynature(arr1)