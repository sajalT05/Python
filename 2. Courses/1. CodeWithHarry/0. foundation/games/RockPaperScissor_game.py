# create a fucntion of game
# rock paper scissor
# rock<paper : rock>scissor
# paper>rock : paper<scissor
# scissor<rock : scissor>paper

# charcaters assignment to options
# rock: r | paper: p | scissor:s

# import radncom module
import random

# choose computer option 
# computerRandomOption --> is string variable
# computerOption --> game option with computer
computerRandomOption=random.randint(1,3) #range from 1 to 3 is given for random integers
if computerRandomOption==1:
    computerOption="r"
elif computerRandomOption==2:
    computerOption="p"
elif computerRandomOption==3:
    computerOption="s"
# computer optiOn is taken

# take user option
# print instructions
print("Welcome, to the game. \nRock: r\nPaper: p\nScissor: s")
# take user options
userOption=input("Enter your option: ")
# show user option
print(f"Your option is {userOption}") 
# show computer option
print("Computer option is", computerOption)

# create a function
# return True for user win and return false for user loose
def rpsGame (comp,user):
    if comp==user:
        return None
    elif comp=="r":
        if user=="p":
            return True
        elif user=="s":
            return False
    elif comp=="p":
        if user=="r":
            return False
        elif user=="s":
            return True
    elif comp=="s":
        if user=="r":
            return True
        elif user=="p":
            return False

# call and assign game function to a new variable
# assign computerOption and userOption as arguments in the funciton
gameVariable=rpsGame(computerOption,userOption)  
if gameVariable==None:
    print("The game is a tie.")
elif gameVariable==True:
    print("Congratulations, you won.")
elif gameVariable==False:
    print("Sorry, you loose.")