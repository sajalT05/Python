# create class
class Class:
    # create methods
    # constructor
    # assign arguments passed in class instance to self variables.
    def __init__(self,argumentNumber1,argumentNumber2):
        self.argumentNumber1=argumentNumber1
        self.argumentNumber2=argumentNumber2
        print("string representation")
    # return as string method
    # return an output in desired string format
    # __str__
    def __str__(self):   
        # return as string output:
        # (integerArgument(1),integerArgument(2))
        return f"Arguments: ({self.argumentNumber1},{self.argumentNumber2})"

# create instance using class
# create object with gicing arguments to class
object=Class(5,6)
# print object
print(object)