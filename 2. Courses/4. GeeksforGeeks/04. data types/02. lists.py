# creating a list
list=[565,256,'string',[1,2,3],256,'string',[1,2,3]]
number_list=[5,8,9,7,6,5,4,3,2,1]

# printing list
print(list)

# size of list
print(len(list))

# index()
'''
returns the index of the first element with the specified value
'''
print(list.index('string'))

# count()
'''
count the number of elements with the specified value
'''
print(list.count('string'))

# sort()
'''
sort the list in ascending order
'''
print(number_list.sort())

# reverse()
'''
reverse the list
'''
print(number_list.reverse())