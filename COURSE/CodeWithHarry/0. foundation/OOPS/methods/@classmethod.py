'''
Class Method:
1. bound to the class and not the object of the class.
2. class attribute is changed.

Decorator used:
@classmethod 
'''
class Class:
    integerVariable=175
    integerVariableClassMethod=642
    # create a normal method
    def method(self,variable):
        self.integerVariable=variable
    # create a method using class method
    @classmethod
    def classMethod(self,classMethodVariable):
        self.integerVariableClassMethod=classMethodVariable


object=Class()
# print class attributes
print("print class attributes...")
print(object.integerVariable)
print("\n")
# use normal method
print("use normal method")
# call method on object
object.method(795)
# print class attributes after using normal method
print("print class attributes after using normal method...")
#  print class attribute in instance
print("print class attribute in instance...")
print(object.integerVariable)
#  print class attribute in class
print("print class attribute in class...")
print(Class.integerVariable)
#  attribute value is not changed in actual class but in the instance.
print("'attribute value is not changed in actual class but in the instance.'\n")

# class method
print("'class method'\n")
# create an another instance
# create object for class method
objectClassMethod=Class()
# print class attributes
print("print class attributes...")
print(objectClassMethod.integerVariableClassMethod)
# use class method
print("use class method")
# call class method on object
objectClassMethod.classMethod(594)
# print class attributes after using class method
print("print class attributes after using class method...")
#  print class attribute in instance
print("print class attribute in instance...")
print(objectClassMethod.integerVariableClassMethod)
#  print class attribute in class
print("print class attribute in class...")
print(Class.integerVariableClassMethod)

#  attribute value is changed in actual and in the instance.
print("'attribute value is changed in actual class and in the instance.'\n")


