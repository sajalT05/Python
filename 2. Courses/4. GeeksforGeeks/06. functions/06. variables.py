'''
a variable defined before function can be used in a function.
to make changes in a variable defined inside a function, use global keyword.
'''

# local variable: defined inside a function. not accessible outside the function.
def functionName():
    localVariable = "local variable"
    print(localVariable)

variableName="outside function variable"
functionName()
print(variableName)

# global variable: defined outside a function. accessible outside the function.
'''
use keyword to define a variable: global
'''
def functionGlobalName():
    """
    using global keyword, define a global variable
    """
    # add new string to global variable
    global globalVariable 
    globalVariable += " .This is Global variable addition."
    print(globalVariable)
    # assign new value to global variable
    globalVariable = "This is new Global variable assignment."
    print(globalVariable)

globalVariable="This is Global variable."
functionGlobalName()