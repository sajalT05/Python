# check a fibonacci number
'''
follows formulae, if any of the two is perfect square, then it is fibonacci number:
(5*n2 + 4) or (5*n2 – 4)

n: number
'''

import math

# create function for perfect square
def perfectsquareroot(x):
    # find square root
    # convert into int
    sqrt=int(math.sqrt(x))
    # return true or false for perfect square
    return(sqrt**2==x)
    
def fibonaccinumber(x):
    # return true if any of the below condition is true
    return perfectsquareroot(5*x**2+4) or perfectsquareroot(5*x**2-4)

def checkfibonacci(x):
    # check if number is fibonacci
    if fibonaccinumber(x):
        print("Fibonacci number")
    else:
        print("Not a Fibonacci number")


# check functions
checkfibonacci(89)