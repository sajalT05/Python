# create a class as remote
class Remote:
    # skip
    pass

# create a class as player
class Player:
    # create a method on moving right
    def moveRight(self):
        # skip
        pass
    def moveLeft(self):
        # skip
        pass


# create an instance for moving player left
# if remote is pressed left, move player to the left
# create a remote1 instance
# create player1 instance 
remote1=Remote()
player1=Player()
# create a condition to move player1 to the left when remote1 is pressed left
# isLeftPressed is a layer of abstraction as a function
if(remote1.isLeftPressed()):
    player1.moveLeft()