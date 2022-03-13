'''
Static method decorator
// self parameter is not used
// returns error on using self parameter
// @staticmethod is a mandatory decorator
'''


# create a class
class User:
    # methods
    # create a static function
    # no need to use self parameter
    @staticmethod
    def greetUser():
        print("Good Morning")

# create object/instance
sajal=User()
# call static function
sajal.greetUser()

    