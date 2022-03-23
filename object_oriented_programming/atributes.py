'''
Types of attributes:
1. Class attributes: instances defined in a class. belongs to a class.
2. Instance attributes: instances defined in an instance. belongs to an instance.

Instance attributes>Class attributes
instance attributes takes preference over class attributes during assignment and retrieval.
'''
# create a class
class Class:
    # create class attributes
    classStringAttribute="String"
    classIntegerAttribute=100

# create an instance
# create and assign an object to a class
object=Class()
# create object attributes
object