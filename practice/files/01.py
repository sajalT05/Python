# 01
# create a game to play a game and return with a score, if high score reached, update high score file and show
import os

# create a game
def game():
    # ask for an integer input
    userNumber=int(input("Enter a number: "))
    # return the number
    return userNumber

# assign game score to a variable
# when variable is assigned, funciton is called.
newScore=game()

# fetch score from the file
# use with statment
with open("/laboratory/python/python learning/resources/score.txt") as file:
    # create a variable to assign score in file
    # convert file text to integers
    score=int(file.read())

# if-else conditional operations
# if newscore is greater than old score
if newScore>score:
    # write the high score file with nwe score
    with open("/laboratory/python/python learning/resources/score.txt", "w") as file:
        # overwrites the old score
        # assign a new variable for updated score
        # convert the new score integer into string before writing in the file
        file.write(str(newScore))  

# 
with open("/laboratory/python/python learning/resources/score.txt") as file:
    updatedScore=file.read()
print("Highest score is,", updatedScore)
