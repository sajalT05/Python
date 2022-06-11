# swap elements in a list

def swaplistelements(list,x,y):
    temp=list[x]
    list[x]=list[y]
    list[y]=temp
    print(list)

# test
list=[5,8,3,12,56,1,2,4]
swaplistelements(list,2,5)