'''
first class function: function can be used and passed as arguments.
first class objects: objects that can be used as variables.
'''

# function are objects
def functionName1(argument):
    return argument.capitalize()
print(functionName1("parameter"))
functionName1_1=functionName1
print(functionName1_1('testing_1'))

# functions are passed as arguments to other functions
def functionName2(argument):
    return argument.upper()
def functionName3(argument):
    return argument.lower()
def functionName4(functionArgument):
    # store function called as variable
    functionVariable=functionArgument("hello man")
    print(functionVariable)
functionName4(functionName2)
functionName4(functionName3)

# function can return another function
def functionName5(arg):
    def functionName6(arg2):
        return arg + arg2
    return functionName6
print(functionName5(10)(20))
functionName7=functionName5(11)
print(functionName7(21))

    

