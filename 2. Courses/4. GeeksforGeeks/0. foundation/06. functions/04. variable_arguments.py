'''
*args: pass through all arguments. 
**kwards: pass through all keyword arguments
'''

# *args: use any name in stead of args
def functionNameArgs(*args):
    print(args)
# call function
functionNameArgs('argument1', 'argument2', 'argument3')

# **kwargs: use any name in stead of kargs
def functionNameKwargs(**kwargs):
    print(kwargs)
# call function
functionNameKwargs(keywrod_argument="keyword_argument_parameter")

