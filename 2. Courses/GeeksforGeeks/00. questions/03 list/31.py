# sort first list using second list

list1=['a','b','c','d','e','f','g']
list2=[1,5,8,7,3,2,4]

def sortlist(l1,l2):
    # zip lists
    zipList=zip(l2,l1)
    # sort zipped list
    zipListSorted=[x for x in sorted(zipList)]
    return list(list(zip(*zipListSorted))[1])

print(sortlist(list1,list2))
