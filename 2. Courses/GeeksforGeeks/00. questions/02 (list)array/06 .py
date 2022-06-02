# remainder of array multiplication divided by array length
'''
avoid overflow
distributive properties of modular arithmetic
( a * b) % c = ( ( a % c ) * ( b % c ) ) % c 
'''
from functools import reduce
def arraymultiplicationremainder(arr):
    arraymultiplication=reduce(lambda x,y:x*y,arr)
    arraylength=len(arr)
    remainder=arraymultiplication%arraylength
    print(remainder)

# call
arr=[1,2,3,4,5,6,7,8,9,10,11,56]
arraymultiplicationremainder(arr)









