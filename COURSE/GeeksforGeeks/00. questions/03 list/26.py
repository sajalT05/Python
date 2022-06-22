# print duplicates in a list of integer

list=[1,5,9,8,1,8,23,6,7,9]

for i in list:
    if list.count(i)>1:
        print(i)

