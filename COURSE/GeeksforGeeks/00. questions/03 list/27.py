# cumulative sum of a list

list=[1,2,3,4,5,6,7,8,9,10]

def cumulativelist(list):
    newlist=[]
    for i in range(len(list)):
        newlist.append(sum(list[:i+1]))
    return newlist    

# test
print(cumulativelist(list))