set1={1,5,9}
set2={'hi','bye'}

# print id
print(id(set1))
print(id(set2))

# print hash
try:
    print(hash(set1))
    print(set1.__hash__())
    print(hash(set2))
    print(set2.__hash__())
except TypeError:
    print("sets are unhashable")
