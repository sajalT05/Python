string1='hello'
string2="bye"

# print id
print(id(string1))
print(id(string2))

# print hash
print(hash(string1))
print(string1.__hash__())
print(hash(string2))
print(string2.__hash__())