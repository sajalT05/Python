# match: compares a subject value against one or more literals

# create a function http_error with argument as status
# match the value passed and return a message
# value passed is the status i.e. argument
def http_error(status):
    # match value of status
    match status:
        #   match single value
        case 404:
            print("Not found")
        # match multiple values
        case 418 | 420 | 421:
            print("I'm a teapot")
        # _ is a wild card. if no case matches, theis is executed.
        case _:
            print("Something's wrong with the internet")
# check function by passing status as argument 
http_error(420)

