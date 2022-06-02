list1=[1,5,9]
list2=['hi','bye']

# print id
print(id(list1))
print(id(list2))

# print hash
try:
    print(hash(list1))
    print(list1.__hash__())
    print(hash(list2))
    print(list2.__hash__())
except TypeError:
    print("lists are unhashable")