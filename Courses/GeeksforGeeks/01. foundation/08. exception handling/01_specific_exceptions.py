# create function
def function(a):
    if a<7: # for a values more than 3
        value=a/(a-5) # error for a=5 --> zero division
    print(value) # error for values of a less than 7
    
# call function
try:
    # a<7 # a!=5 --> no error
    function(3)
    # a=5 --> ZeroDivisionError: division by zero
    function(5)
    # a>7 --> UnboundLocalError
    function(7)
except ZeroDivisionError:
    print('ZeroDivisionError')
except UnboundLocalError:
    print('UnboundLocalError')
except NameError:
    print("NameError Occurred and Handled")
else:
    print("No Error Occurred")
finally:
    print("Finally Block Executed")