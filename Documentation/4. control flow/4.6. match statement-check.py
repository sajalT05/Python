# match: compares a subject value against one or more literals

# same like switch-case

# integers as argument
def http_error(status):
    # match value of status
    match status:
        #   match single value
        case 404:
            print("Not found")
        # match multiple values
        case 418 | 420 | 421:
            print("I'm a teapot")
        # _ is a wild card. if no case matches, this is executed.
        case _:
            print("Something's wrong with the internet")
# check function by passing status as argument 
http_error(420)

# tuple as argument
def point(x,y):
    # point is an (x, y) tuple
    match point:
        case (0,0):
            print("Origin")
        case (0, y):
            print(f"Y={y}")
        case (x, 0):
            print(f"X={x}")
        case (x, y):
            print(f"X={x}, Y={y}")
        case _:
            raise ValueError("Not a point")
# check function by passing status as argument 
point(5,0)
