# check elements in list

from turtle import position


list=[5,8,3,12,56,1,2,4]

def numberinlist(x):
    try:
        position=list.index(x)
        print("The number",x,"is in position",position)
    except ValueError:
        print("The number",x,"is not in the list")

# test
numberinlist(89)
