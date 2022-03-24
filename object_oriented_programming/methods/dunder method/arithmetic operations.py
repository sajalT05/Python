'''
Dunder Method:
1. operators in python can be overloaded using dunder method.
2. these methods are called when operators are used on the objects.

Rules:
1. methods are used automatically, when the operator is used.
2. important to define methods 'code'.

Important:
__str__ : 
    a. represent a class object/instance as a string.

'''

# create a class
from numpy import product


class Class:
    # create a constructor
    # fetch argument while instance creation
    def __init__(self,argumentNumber):
        # assign argument number to number
        self.argumentNumber=argumentNumber
    
    # create dunder method
    # addition method
    # __add__
    def __add__(self,argumentNumber2):
        print("addition")
        # return addition:
        # integerArgument(1) + integerArgument(2)
            # number passed as argument in self instance
            # number passed as argument in other instance using same class
        return self.argumentNumber + argumentNumber2.argumentNumber
    # multiplication method
    # __mul__
    def __mul__(self,argumentNumber2):
        print("multiplication")
        # return addition:
        # integerArgument(1) * integerArgument(2)
            # number passed as argument in self instance
            # number passed as argument in other instance using same class
        return self.argumentNumber * argumentNumber2.argumentNumber
    # substraction method
    # __sub__
    def __sub__(self,argumentNumber2):
        print("substraction")
        # return addition:
        # integerArgument(1) - integerArgument(2)
            # number passed as argument in self instance
            # number passed as argument in other instance using same class
        return self.argumentNumber - argumentNumber2.argumentNumber
    # division method
    # __truediv__
    def __truediv__(self,argumentNumber2):
        print("division")
        # return addition:
        # integerArgument(1) / integerArgument(2)
            # number passed as argument in self instance
            # number passed as argument in other instance using same class
        return self.argumentNumber / argumentNumber2.argumentNumber
    # remainder method
    # __floordiv__
    def __floordiv__(self,argumentNumber2):
        print("remainder")
        # return addition:
        # integerArgument(1) // integerArgument(2)
            # number passed as argument in self instance
            # number passed as argument in other instance using same class
        return self.argumentNumber // argumentNumber2.argumentNumber



# create instance using class
# create object n1
n1=Class(500)
# create object n2
n2=Class(11)

# sum of objects
summation = n1 + n2
    # print
print(sum)
# product of objects
product = n1 * n2
    # print
print(product)
# difference of objects
difference = n1 - n2
    # print
print(difference)
# division of objects
division = n1 / n2
    # print
print(division)
# remainder during division of objects
remainder = n1 // n2
    # print
print(remainder)
