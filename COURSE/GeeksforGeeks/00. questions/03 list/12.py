# n largest number in a list

def nlargestnumberlist(list,n):
    list.sort()
    print(list[-n])

# test
list=[5,8,3,12,56,1,2,4]
nlargestnumberlist(list,3)
