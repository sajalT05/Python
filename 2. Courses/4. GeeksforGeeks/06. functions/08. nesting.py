'''
nested function: function defined in other function.
'''

def outerFunction(arg):
    arg=arg
    def innerFunction():
        print(arg)
    innerFunction()

outerFunction("hi")

if __name__=="__main__":
    # run the code in the current file
    closureFunction=outerFunction("hello")
    closureFunction()