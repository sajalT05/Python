# remove empty tuples from a list

list=[(),(1),('a',),(1,2),(1,2,3)]

for i in list:
    if len(i)==0:
        list.remove(i)
print(list)