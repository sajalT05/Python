list=[1,5,9,11,15,19, 22, 22, 24, 26, 30, 30]

# uses () instead of []. same as list comprehension
generator_comprehension=(value*2 for value in list if value%2==0)
print("generator comprehension:",)
for value in generator_comprehension:
    print(value)
