dict1={"key1":"value1","key2":"value2"}
dict2={"a":1,"b":2}

# print id
print(id(dict1))
print(id(dict2))

# print hash
try:
    print(hash(dict1))
    print(dict1.__hash__())
    print(hash(dict2))
    print(dict2.__hash__())
except TypeError:
    print("dictionaries are unhashable")
