'''
send sequence of values when function is called
'''

# generator_function: function that yields values
def generator_function():
    yield 1
    yield 2
    yield 3

# generator_object: used to call generator_function
generator_object=generator_function()

print(generator_object.next())