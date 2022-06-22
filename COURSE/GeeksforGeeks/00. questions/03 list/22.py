# remove empty list from list

list=[[],['a'],[1]]

for i in list:
    if len(i)==0:
        list.remove(i)
print(list)