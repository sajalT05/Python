# create function
def function(a):
    if a>7: # for a values more than 3
        value=a/(a-5) # error for a=5 --> zero division
    print(value) # error for values of a less than 7
    
# call function
function(1)

