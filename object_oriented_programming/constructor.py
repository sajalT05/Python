# create class
# create user class
# default self parameter constructors
class Message:
    # method
    # create constructor
    # automatically called when object is created
    # executed as soon as a new object is created
    # no need to assign any other attributes or call __init__()
    # just self argument/parameter
    def __init__(self):
        print(f"New object created.")
        # returns -> New object created.
# create user details class
# default and additional arguments
class User:
    # method
    # constructor
    # place multiple arguments
    def __init__(self,name,age,salary,address):
        # name is user name
        self.name=name
        # age is user age
        self.age=age
        # salary is users salary
        self.salary=salary
        # office is users office address
        self.address=address
        print(f"User {name} with {age}, and salary {salary}.\nAddress: {address}")
        


# create a greet object with message class
greet=Message()

# create a sajal object with user class
# define all other arguments (name,age,salary,office)
sajal=User('Sajal Tiwari',25,"1,000,000,000 Indian Rupees",'''"H-BB2", Jain Tower, 'Bal Mandir Road'.''')