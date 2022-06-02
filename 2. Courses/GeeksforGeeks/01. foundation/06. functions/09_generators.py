def generatorFunction():
    yield "value1"
    yield "value2"
    yield "value3"

for value in generatorFunction():
    print(value)

object=generatorFunction()

# print(next(object))
print(object.__next__())
print(object.__next__())
print(object.__next__())