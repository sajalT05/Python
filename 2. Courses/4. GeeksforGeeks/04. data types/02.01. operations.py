list=[1,'string',[1,2,3],1,'string',[1,2,3]]

# adding element to list
# append()
list.append(256)
print(list)
# insert()
'''add element at a secific position of a list
'''
list.insert(0,'256')
print(list)
# extend()
'''
adding multiple elements at the end of list
'''
list.extend(['string1','string2'])
print(list)
# indexing
print(list[2])
# slicing
'''
show specific portionof string'''
print(list[2:5])
# removing element from list
# remove()
'''
remove element one time
'''
list.remove('string')
print(list)
# pop()
'''
removes elemenmts from the end or at a position
'''
list.pop()
print(list)
list.pop(3)
print(list)