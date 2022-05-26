# # --> depreciated


# # import random module
# import random

# # create a function for computer output
# def computerOutput():
# # fetch random numbers
# # use random module
# # randomNumber --> random number integer variable
#     randomNumber=random.randint(1,2,3)
# # assign random integers to game options,i.e. 1,2,3
# # computerOption --> variable to assign game option to computer
#     if randomNumber==1:
#         computerOption="r"
#     elif randomNumber==2:
#         computerOption="p"
#     elif randomNumber==3:
#         computerOption="s"
#     print(f"Computer Option is {computerOption}")



# # instruct user to enter an option
# print("Welcome, to the game. \nRock: r\nPaper: p\nScissor: s")
# # create a function to get user input
# def userInput():
# # while loop --> will return to initial command if wrong option is selected
#     while True:
#         userOption=input("Enter your option: ")
# # userOption --> user option selected
# # lower() function used to return the input into lowercase
#         if userOption=="s" or userOption=="r" or userOption=="p": #instruct computer to check options
#             print(f"Your option is {userOption}")
#         else:
#             print("Pleae choose the right option.")
#             userInput()

# # call userInput() function
# userInput()

# # call computerOutput() function
# computerOutput()


