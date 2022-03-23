'''
Setter method:
    a. behaves as a proeprty. similar to class variables.
    b. 

Rules:
    a. getter method has to be used before setter method on a function.
    b. assign a function using getter method. 
    --> if @property is not used, i.e. getter method
       //  setter method will return an error.
            >   NameError: name 'functionName' is not defined
    c. property instance value is changed.

Decorator used:
@functionName.setter

'''
# create class
class Class:
    # create variables
    integerVariable1=101
    integerVariable2=202
    # integerVariableSum=303

# property method is used, i.e. getter method. A function is created
#  integerVariableSumfunctionName is a function of sum of integers, 
    #   class attributes.

    @property
    def integerVariableSumfunctionName(self):
        # use return when need to get value --> error received when return not used.
        return self.integerVariable1+self.integerVariable2

    @integerVariableSumfunctionName.setter
    def integerVariableSumfunctionName(self,variable):
        '''
        1. new value for integerVariable2 is obtained with argument passed.    
        2. value of integerVariable1 is used as in class attribute.
        3. variable value is defined in instance.
        4. new integerVariable2 is equal to
            --> new argument passed in property call minus integerVariable1
        '''
        self.integerVariable2=variable-self.integerVariable1

# create instance of class
# create object
# use (), parenthesis while assigning class to an object. --> error made.
object=Class()
# assign value to object property
    # use setter method which is now a property property   
# print class attributes
# before assigning property value
print("print class attributes, before assigning property value.")
print(f"constant integerVariable1: {object.integerVariable1}")
print(f"old integerVariable2: {object.integerVariable2}")
# print property method value
print("print property method value, i.e. sum.")
print(f"integerVariableSumfunctionName: {object.integerVariableSumfunctionName}")
print("\n")

# assign property value, --> used setter method
object.integerVariableSumfunctionName=500
# after assigning property value
print("print class attributes, after assigning property value.")
print(f"integerVariable1: {object.integerVariable1}")
print(f"new integerVariable2: {object.integerVariable2}")
print("\n")

# checking property value in class
# print("checking property value in class")
# print(Class.integerVariableSumfunctionName) --> returns <property object at 0x000001FCA9E88D60>

# checking property value while creating another instance
print("checking property value while creating another instance")
# create a new instance to class
# create a new object
newObject=Class()
# check value of class attributes
print("check value of class attributes")
print(f"newObject integerVariable1: {newObject.integerVariable1}")
print(f"newObject integerVariable2: {newObject.integerVariable2}")
'''
// class attribute value is not changed. 
    // when created new object and checked attributes values.
    // value defined in class defined is returned.
'''
