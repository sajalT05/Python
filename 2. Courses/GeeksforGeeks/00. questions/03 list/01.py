# interchange first and last element in a list

list=[5,8,3,12,56,1,2,4]
temp=list[0]
list[0]=list[-1]
list[-1]=temp
print(list)
