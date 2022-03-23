# calculator
# square, square cube and square root of a number

# create a calculator class
from numpy import square


class Calculator:
    # method
    # constructor
    def __init__(self,number):
        # number is an integer argument
        # assign self.number to number Variable
        self.number=number
    # create function for calculation
    def calculation(self):
        # print square
        print(f"Square of number is, {self.number**2}")
        # print cube
        print(f"Cube of number is, {self.number**3}")
        # print square root
        print(f"Square root of number is, {self.number**(1/2)}")
       # print cube root
        print(f"Cube  root of number is, {self.number**(1/3)}")


# create an object num with calculator class and use number 25
num=Calculator(25)
# call square function
num.calculation()
