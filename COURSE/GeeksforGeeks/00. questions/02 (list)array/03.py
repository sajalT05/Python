# rotate array

list=[1,2,3,'a',5,6,7,8,9,10]

def rotatearray(d,arr):
    '''
    arr: array
    d: index
    '''
    arraylength=len(arr)
    # new array
    arr[:]=arr[d:arraylength]+arr[:d]
    print(arr)

# call
rotatearray(4,list)
