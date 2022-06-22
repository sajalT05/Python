# break a list into a n lists

list=[4,44,5,55,6,66,7,77,8,88,9,99,10,100]

def breaklist(list,n):
    ''' 
    break this list into small list of size n
    '''
    # number of possible lists
    listsize=len(list)//n
    # remaining elements number
    leftnumber=len(list)%n
    matrix=[]
    if listsize==0:
        print("not possible to break")
    else:
       for i in range(listsize):
           newlist=[]
           newlist=list[i*n:(i+1)*n]
           matrix.append(newlist)
           print(newlist)
    listofleftnumbers=list[-leftnumber:]
    print(listofleftnumbers)
    matrix.append(listofleftnumbers)

    print(matrix)

# call
# print(len(list))
breaklist(list,3)

    