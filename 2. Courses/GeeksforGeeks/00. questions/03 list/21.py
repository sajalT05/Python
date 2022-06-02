# remove multiple elements from list

list=[5,8,3,12,56,1,2,415,5,8,2,1]

for i in list:
    if list.count(i)>1:
        list.remove(i)
print(list)