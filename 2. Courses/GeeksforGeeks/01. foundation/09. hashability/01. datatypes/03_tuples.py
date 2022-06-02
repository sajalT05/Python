tuple1={1,5,9}
tuple2=('hi','bye')

# print id
print(id(tuple1))
print(id(tuple2))

# print hash
try:
    print(hash(tuple1))
    print(tuple1.__hash__())
    print(hash(tuple2))
    print(tuple2.__hash__())
except TypeError:
    print("tuples are unhashable")