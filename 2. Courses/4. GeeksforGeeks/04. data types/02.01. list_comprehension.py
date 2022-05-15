'''
creating a new list from other data types
'''

list=[131,'string',[13,2,3],131,'string',[13,2,3]]
new_list=[str(num) for num in list]
print(new_list)
