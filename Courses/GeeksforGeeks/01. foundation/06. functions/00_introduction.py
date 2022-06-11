'''
function: methods in python. block of statements that can be resued to perform a task.
argument: parameters that are passed to a function when called.
default_argument: argument with a default value.
keyword_argument: argument with a keyword used when called.
doc-string: first documentation string in a function.
    -->
    accessed by functionName.__doc__
return: value that a function returns.
'''
def functionName(argument):
    """
    doc-string
    """
    return None

# calling function
functionName("parameter")


# function with argument, keyword argument, default argument
def functionName(argument, keyword_argument, default_argument="default value"):
    """
    doc-string
    """
    print(argument, keyword_argument, default_argument)

# calling function
functionName("parameter", keyword_argument="keyword_argument_parameter")