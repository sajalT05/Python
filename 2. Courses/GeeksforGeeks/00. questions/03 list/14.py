# odd numbers in a list

list=[5,8,3,12,56,1,2,4]
oddlist=[]
for i in list:
    if i%2!=0:
        oddlist.append(i)
print(oddlist)