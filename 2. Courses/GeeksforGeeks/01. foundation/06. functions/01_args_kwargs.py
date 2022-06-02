# *args
def arg_function1(*args):
    for arg in args:
        print(arg)
arg_function1("a", "b", "c", 1, 2, 3)

# arg and *args
def arg_function2(arg, *args):
    # arg
    print("arg:", arg)
    # *args
    for arg in args:
        print("*args:", arg)
arg_function2("a", "b", "c", 1, 2, 3)

# **kwargs
def arg_function3(**kwargs):
    for key, value in kwargs.items():
        print(f"key: {key}, value: {value}")
arg_function3(a="a", b="b", c="c", d="d", e="e")

# args, *args, and **kwargs
def arg_function4(arg, *args, **kwargs):
    # arg
    print("arg:", arg)
    # *args
    for arg in args:
        print("*args:", arg)
    # **kwargs
    for key, value in kwargs.items():
        print(f"key: {key}, value: {value}")
arg_function4("a", "b", "c", 1, 2, 3, a="a", b="b", c="c", d="d", e="e")


# *args and **kwargs
def arg_function5(*args, **kwargs):
    print("*args:", args)
    print("**kwargs:", kwargs)
arg_function5("a", "b", "c", 1, 2, 3, a="a", b="b", c="c", d="d", e="e")
