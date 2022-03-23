''''
property method: 
    also known as getter method.

syntax used: 
@property

e.g.
class Class:
    @property
    def functionName(self):
        // statements

1. function behaves like a property, i.e. attributes.
2. () parenthesis are not used.
'''

class Class:
    integer1=102
    integer2=265
    # find sum of integer
    '''
    create a property'''
    # function as a property
    # sum of inetgers 
    @property
    def integerSum(self):
        print(self.integer1 + self.integer2)

# instance of class
value=Class()
# call function as a property
# print the value
'''
() is not used while calling property
'''
value.integerSum