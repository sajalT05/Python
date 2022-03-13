'''
dictionary: collection of key value pairs
1. it is unordered
2. mutable, i.e. it can be changed.
3. it is indexed, position are assigned to key-vcalue pairs
4. cannot contain duplicate pairs.
5. classifying element is key and classified element is calue.
'''
# create a dicitonary

myDictionary = {
    "key":"value",
    "str":"string name",
    "int":5,
    "list":[1,5,"name"],
    "dict":{"name":"sajal","age":25},
    1:2
    }


# dictionary methods
print(myDictionary) #print dictionary
print(myDictionary.items()) #returns key-value pairs/tuples
print(myDictionary.keys()) #returns all keys in dictionary
print(myDictionary.values()) #returns all values in dictionary
print(myDictionary.get("key")) #returns value of the key
print(myDictionary["key"]) #print values of a key in dictionary
# //dictionary.get("key_not_present") method returns none if key not present.
# //dictionary["key_not_present"] method returns error if key is not present --> never use for dictinary 
myDictionary["int"]=25 #change value of a key in a dictionary
print(myDictionary["int"]) #print updated value of a key after changing
# print(myDictionary["list"]["dictionary"])
## update and print //like sorting/updating/appending lists
myDictionary.update({"new_key":"new value"}) #add new key-value tuple like a seprate dicitonary
print(myDictionary)
