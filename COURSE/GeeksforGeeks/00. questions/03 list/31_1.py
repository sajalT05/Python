# sort first list using second list

list1=['a','b','c','d','e','f','g']
list2=[1,5,8,7,3,2,4]

def sortlist(l1,l2):
    # create empty dictionary
    dict={}
    # add list elements as key and values
    # list to 
    dict={l1[i]:l2[i] for i in range(len(l1))}
    # print(dict)
    # sort ditionary
    dictSort={k:v for (k,v) in sorted(dict.items(), key=lambda item:item[1])}
    # print(dictSort)
    # create list with keys
    newlist=[item for item in dictSort.keys()]
    print(newlist)


sortlist(list1,list2)